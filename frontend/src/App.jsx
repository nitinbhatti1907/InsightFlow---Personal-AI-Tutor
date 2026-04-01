import { useEffect, useMemo, useState } from 'react';
import {
  api,
  clearAuthSession,
  getStoredUser,
  storeAuthSession,
} from './api/client';
import ActivityLogPanel from './components/ActivityLogPanel';
import AuthPanel from './components/AuthPanel';
import DashboardPanel from './components/DashboardPanel';
import FeedbackForm from './components/FeedbackForm';
import Hero from './components/Hero';
import LearnerProgressPanel from './components/LearnerProgressPanel';
import LearningOutput from './components/LearningOutput';
import LearnMorePanel from './components/LearnMorePanel';
import QuizPanel from './components/QuizPanel';
import TopicExplorer from './components/TopicExplorer';

const initialForm = {
  topic_id: 'pandas-core',
  topic_query: '',
  proficiency_level: 'beginner',
  learning_style: 'visual',
  detail_mode: 'standard',
  include_resources: true,
  include_quiz: true,
};

const initialAuthForm = {
  full_name: '',
  email: '',
  password: '',
};

export default function App() {
  const [overview, setOverview] = useState(null);
  const [topics, setTopics] = useState([]);
  const [dashboard, setDashboard] = useState(null);
  const [learnerOverview, setLearnerOverview] = useState(null);
  const [form, setForm] = useState(initialForm);
  const [content, setContent] = useState(null);
  const [learnMore, setLearnMore] = useState(null);
  const [quizAnswers, setQuizAnswers] = useState([]);
  const [quizResult, setQuizResult] = useState(null);
  const [feedbackSuccess, setFeedbackSuccess] = useState('');
  const [lessonActionMessage, setLessonActionMessage] = useState('');
  const [authMode, setAuthMode] = useState('login');
  const [authForm, setAuthForm] = useState(initialAuthForm);
  const [user, setUser] = useState(getStoredUser());
  const [loadingState, setLoadingState] = useState({
    bootstrap: true,
    auth: false,
    logout: false,
    generate: false,
    learnMore: false,
    quiz: false,
    feedback: false,
    markRead: false,
  });
  const [error, setError] = useState('');
  const [generateError, setGenerateError] = useState('');
  const [feedback, setFeedback] = useState({
    learner_name: 'Anonymous',
    rating: 5,
    comment: '',
  });

  const topicsMap = useMemo(
    () => Object.fromEntries(topics.map((topic) => [topic.id, topic.title])),
    [topics]
  );

  const completedTopicIds = learnerOverview?.completed_topic_ids || [];
  const isCurrentTopicRead = content ? completedTopicIds.includes(content.topic_id) : false;

  async function loadProtectedData() {
    const [dashboardData, learnerOverviewData] = await Promise.all([
      api.getDashboard(),
      api.getLearnerOverview(),
    ]);
    setDashboard(dashboardData);
    setLearnerOverview(learnerOverviewData);
  }

  useEffect(() => {
    async function bootstrap() {
      try {
        const [overviewData, topicsData] = await Promise.all([
          api.getOverview(),
          api.getTopics(),
        ]);
        setOverview(overviewData);
        setTopics(topicsData);

        if (user) {
          try {
            const me = await api.me();
            setUser(me);
            storeAuthSession(localStorage.getItem('learning_assistant_token'), me);
            await loadProtectedData();
            setFeedback((current) => ({ ...current, learner_name: me.full_name }));
          } catch {
            clearAuthSession();
            setUser(null);
          }
        }
      } catch {
        setError('Could not connect to the backend. Start the FastAPI server first.');
      } finally {
        setLoadingState((current) => ({ ...current, bootstrap: false }));
      }
    }

    bootstrap();
  }, []);

  const updateForm = (field, value) => {
    setGenerateError('');
    setLessonActionMessage('');
    setForm((current) => ({ ...current, [field]: value }));
  };

  const updateAuthForm = (field, value) => {
    setAuthForm((current) => ({ ...current, [field]: value }));
  };

  const updateFeedback = (field, value) => {
    setFeedback((current) => ({ ...current, [field]: value }));
  };

  const handleAuthSubmit = async () => {
    setError('');
    setGenerateError('');
    setLoadingState((current) => ({ ...current, auth: true }));

    try {
      const payload =
        authMode === 'register'
          ? {
              full_name: authForm.full_name.trim(),
              email: authForm.email.trim(),
              password: authForm.password,
            }
          : {
              email: authForm.email.trim(),
              password: authForm.password,
            };

      const response =
        authMode === 'register'
          ? await api.register(payload)
          : await api.login(payload);

      storeAuthSession(response.token, response.user);
      setUser(response.user);
      setFeedback((current) => ({ ...current, learner_name: response.user.full_name }));
      setAuthForm(initialAuthForm);
      await loadProtectedData();
    } catch (authError) {
      setError(authError.message || 'Authentication failed.');
    } finally {
      setLoadingState((current) => ({ ...current, auth: false }));
    }
  };

  const handleLogout = async () => {
    setLoadingState((current) => ({ ...current, logout: true }));
    try {
      await api.logout();
    } catch {
      // ignore and clear local session anyway
    } finally {
      clearAuthSession();
      setUser(null);
      setLearnerOverview(null);
      setDashboard(null);
      setContent(null);
      setLearnMore(null);
      setQuizResult(null);
      setQuizAnswers([]);
      setFeedbackSuccess('');
      setLessonActionMessage('');
      setGenerateError('');
      setLoadingState((current) => ({ ...current, logout: false }));
    }
  };

  const refreshUserPanels = async () => {
    if (!user) return;
    const [dashboardData, learnerOverviewData] = await Promise.all([
      api.getDashboard(),
      api.getLearnerOverview(),
    ]);
    setDashboard(dashboardData);
    setLearnerOverview(learnerOverviewData);
  };

  const handleGenerate = async () => {
    setError('');
    setGenerateError('');
    setFeedbackSuccess('');
    setLessonActionMessage('');
    setLoadingState((current) => ({ ...current, generate: true }));
    setLearnMore(null);
    setQuizResult(null);

    const isOther = form.topic_id === 'others';
    const cleanedQuery = isOther ? form.topic_query.trim() : '';
    const payload = {
      ...form,
      topic_id: isOther ? null : form.topic_id,
      topic_query: cleanedQuery,
    };

    try {
      const response = await api.generateContent(payload);
      setContent(response);
      setQuizAnswers(new Array(response.quiz.length).fill(-1));
      setFeedback((current) => ({ ...current, comment: '' }));
      await refreshUserPanels();
    } catch (requestError) {
      setGenerateError(
        requestError.message || 'Generation failed. Please verify the backend is running and try again.'
      );
    } finally {
      setLoadingState((current) => ({ ...current, generate: false }));
    }
  };

  const handleQuizAnswer = (questionIndex, selectedIndex) => {
    setQuizAnswers((current) => {
      const next = [...current];
      next[questionIndex] = selectedIndex;
      return next;
    });
  };

  const handleQuizSubmit = async () => {
    if (!content) return;
    setLoadingState((current) => ({ ...current, quiz: true }));
    setError('');

    try {
      const result = await api.evaluateQuiz({
        topic_id: content.topic_id,
        answers: quizAnswers,
      });
      setQuizResult(result);
      await refreshUserPanels();
    } catch (quizError) {
      setError(quizError.message || 'Quiz evaluation failed.');
    } finally {
      setLoadingState((current) => ({ ...current, quiz: false }));
    }
  };

  const handleLearnMore = async () => {
    if (!content) return;
    setLoadingState((current) => ({ ...current, learnMore: true }));
    setError('');

    try {
      const response = await api.learnMore({
        topic_id: content.topic_id,
        proficiency_level: form.proficiency_level,
        learning_style: form.learning_style,
      });
      setLearnMore(response);
      setLessonActionMessage(`Expanded lesson opened for ${content.topic_title}.`);
      await refreshUserPanels();

      setTimeout(() => {
        document.getElementById('learn-more-panel')?.scrollIntoView({
          behavior: 'smooth',
          block: 'start',
        });
      }, 80);
    } catch (learnMoreError) {
      setError(learnMoreError.message || 'Could not load the Learn More content.');
    } finally {
      setLoadingState((current) => ({ ...current, learnMore: false }));
    }
  };

  const handleMarkRead = async () => {
    if (!content) return;
    setLoadingState((current) => ({ ...current, markRead: true }));
    setError('');

    try {
      const response = await api.markTopicRead({
        topic_id: content.topic_id,
        topic_title: content.topic_title,
      });
      setLessonActionMessage(response.message);
      await refreshUserPanels();
    } catch (markReadError) {
      setError(markReadError.message || 'Could not mark this topic as read.');
    } finally {
      setLoadingState((current) => ({ ...current, markRead: false }));
    }
  };

  const handleFeedbackSubmit = async () => {
    if (!content) {
      setError('Generate a topic first, then save feedback.');
      return;
    }

    setLoadingState((current) => ({ ...current, feedback: true }));
    setError('');

    try {
      await api.submitFeedback({
        learner_name: feedback.learner_name,
        topic_id: content.topic_id,
        proficiency_level: form.proficiency_level,
        learning_style: form.learning_style,
        detail_mode: form.detail_mode,
        rating: feedback.rating,
        quiz_score: quizResult?.score_percent || 0,
        comment: feedback.comment,
      });
      setFeedbackSuccess('Feedback saved. Your learner panels were refreshed.');
      await refreshUserPanels();
    } catch (feedbackError) {
      setError(feedbackError.message || 'Saving feedback failed.');
    } finally {
      setLoadingState((current) => ({ ...current, feedback: false }));
    }
  };

  if (loadingState.bootstrap) {
    return (
      <main className="min-h-screen bg-slate-50 px-6 py-12 lg:px-10">
        <div className="mx-auto max-w-7xl animate-pulse space-y-6">
          <div className="h-52 rounded-[2rem] bg-slate-200" />
          <div className="h-72 rounded-[2rem] bg-slate-200" />
          <div className="h-96 rounded-[2rem] bg-slate-200" />
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-slate-50 px-6 py-10 lg:px-10">
      <div className="mx-auto max-w-7xl space-y-8">
        {!user ? (
          <>
            <Hero overview={overview} />
            <AuthPanel
              mode={authMode}
              form={authForm}
              onChange={updateAuthForm}
              onSubmit={handleAuthSubmit}
              onModeChange={setAuthMode}
              loading={loadingState.auth}
              error={error}
            />
          </>
        ) : (
          <>
            <Hero overview={overview} />

            {error && (
              <div className="rounded-3xl border border-rose-200 bg-rose-50 px-5 py-4 text-sm text-rose-800">
                {error}
              </div>
            )}

            <LearnerProgressPanel
              learnerOverview={learnerOverview}
              user={user}
              onLogout={handleLogout}
              loading={loadingState.logout}
            />

            <TopicExplorer
              topics={topics}
              form={form}
              onChange={updateForm}
              onGenerate={handleGenerate}
              loading={loadingState.generate}
              error={generateError}
            />

            <LearningOutput
              content={content}
              onContinue={handleLearnMore}
              onMarkRead={handleMarkRead}
              continueLoading={loadingState.learnMore}
              markReadLoading={loadingState.markRead}
              isTopicRead={isCurrentTopicRead}
              actionMessage={lessonActionMessage}
            />

            {content && (
              <div className="grid gap-6 xl:grid-cols-[1.05fr_0.95fr]">
                <div className="space-y-6">
                  <QuizPanel
                    quiz={content.quiz}
                    answers={quizAnswers}
                    onAnswerChange={handleQuizAnswer}
                    onSubmit={handleQuizSubmit}
                    result={quizResult}
                    loading={loadingState.quiz}
                  />
                  <FeedbackForm
                    feedback={feedback}
                    onChange={updateFeedback}
                    onSubmit={handleFeedbackSubmit}
                    loading={loadingState.feedback}
                    successMessage={feedbackSuccess}
                  />
                </div>

                <LearnMorePanel
                  data={learnMore}
                  onOpen={handleLearnMore}
                  loading={loadingState.learnMore}
                />
              </div>
            )}

            <div className="grid gap-6 xl:grid-cols-[1fr_1fr]">
              <ActivityLogPanel learnerOverview={learnerOverview} />
              <DashboardPanel dashboard={dashboard} topicsMap={topicsMap} />
            </div>
          </>
        )}
      </div>
    </main>
  );
}