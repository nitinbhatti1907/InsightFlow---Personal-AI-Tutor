export default function LearnerProgressPanel({
  learnerOverview,
  user,
  onLogout,
  loading,
}) {
  const progressPercent = learnerOverview?.progress_percent ?? 0;
  const completedTopics = learnerOverview?.completed_topics ?? 0;
  const topicsLearned = learnerOverview?.topics_learned ?? 0;
  const quizzesCompleted = learnerOverview?.quizzes_completed ?? 0;
  const averageQuizScore = learnerOverview?.average_quiz_score ?? 0;

  return (
    <section className="card-surface p-6 lg:p-8">
      <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
        <div>
          <p className="text-sm font-semibold uppercase tracking-[0.24em] text-brand-600">
            Learner profile
          </p>
          <h2 className="mt-2 text-2xl font-semibold text-slate-900">
            Welcome, {user?.full_name || 'Learner'}
          </h2>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-600">
            Your activity history, quiz performance, and course progress are
            stored here like a personal learning assistant.
          </p>
        </div>

        <button
          type="button"
          onClick={onLogout}
          disabled={loading}
          className="self-start rounded-2xl border border-slate-200 bg-white px-5 py-3 text-sm font-semibold text-slate-700 transition hover:border-brand-200 hover:bg-brand-50 hover:text-brand-700 disabled:cursor-not-allowed disabled:opacity-70"
        >
          {loading ? 'Logging out...' : 'Logout'}
        </button>
      </div>

      <div className="mt-6 grid gap-4 xl:grid-cols-[1.45fr_0.55fr_0.55fr_0.6fr]">
        <div className="rounded-3xl border border-slate-200 bg-gradient-to-br from-slate-50 to-white p-6 shadow-sm">
          <div className="flex items-center justify-between gap-3">
            <p className="text-sm font-semibold uppercase tracking-[0.22em] text-brand-600">
              Course progress
            </p>
            <span className="rounded-full border border-slate-200 bg-white px-3 py-1 text-sm font-medium text-slate-600">
              Completed topics: {completedTopics}
            </span>
          </div>

          <div className="mt-5 text-4xl font-bold tracking-tight text-slate-900">
            {progressPercent}% / 100%
          </div>

          <div className="mt-6 h-4 overflow-hidden rounded-full bg-slate-200">
            <div
              className="h-full rounded-full bg-gradient-to-r from-brand-500 via-blue-500 to-cyan-400 transition-all duration-500"
              style={{ width: `${Math.max(0, Math.min(progressPercent, 100))}%` }}
            />
          </div>

          <p className="mt-6 text-sm leading-6 text-slate-600">
            Progress increases when you complete quizzes with a passing score
            and build coverage across the course topics.
          </p>
        </div>

        <div className="group relative overflow-hidden rounded-3xl border border-blue-100 bg-gradient-to-br from-blue-50 to-cyan-50 p-6 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg">
          <div className="absolute right-0 top-0 h-20 w-20 rounded-full bg-blue-200/40 blur-2xl" />
          <div className="relative">
            <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-2xl bg-blue-500/10 text-xl text-blue-600 shadow-sm">
              📘
            </div>
            <p className="text-sm font-medium text-slate-500">Topics learned</p>
            <div className="mt-5 text-4xl font-bold tracking-tight text-slate-900">
              {topicsLearned}
            </div>
            <p className="mt-4 text-xs font-semibold uppercase tracking-[0.18em] text-blue-700">
              Learning coverage
            </p>
          </div>
        </div>

        <div className="group relative overflow-hidden rounded-3xl border border-emerald-100 bg-gradient-to-br from-emerald-50 to-teal-50 p-6 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg">
          <div className="absolute right-0 top-0 h-20 w-20 rounded-full bg-emerald-200/40 blur-2xl" />
          <div className="relative">
            <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-2xl bg-emerald-500/10 text-xl text-emerald-600 shadow-sm">
              ✓
            </div>
            <p className="text-sm font-medium text-slate-500">Quizzes completed</p>
            <div className="mt-5 text-4xl font-bold tracking-tight text-slate-900">
              {quizzesCompleted}
            </div>
            <p className="mt-4 text-xs font-semibold uppercase tracking-[0.18em] text-emerald-700">
              Practice activity
            </p>
          </div>
        </div>

        <div className="group relative overflow-hidden rounded-3xl border border-violet-100 bg-gradient-to-br from-violet-50 to-fuchsia-50 p-6 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-lg">
          <div className="absolute right-0 top-0 h-20 w-20 rounded-full bg-violet-200/40 blur-2xl" />
          <div className="relative">
            <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-2xl bg-violet-500/10 text-xl text-violet-600 shadow-sm">
              ★
            </div>
            <p className="text-sm font-medium text-slate-500">Average quiz score</p>
            <div className="mt-5 text-4xl font-bold tracking-tight text-slate-900">
              {averageQuizScore}%
            </div>
            <p className="mt-4 text-xs font-semibold uppercase tracking-[0.18em] text-violet-700">
              Performance quality
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}