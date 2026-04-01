from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

LearningStyle = Literal["visual", "hands-on", "reading", "exam-prep"]
ProficiencyLevel = Literal["beginner", "intermediate", "advanced"]
DetailMode = Literal["quick", "standard", "deep"]


class TopicSummary(BaseModel):
    id: str
    title: str
    difficulty: str
    duration: str
    tags: list[str]
    learning_objectives: list[str]


class TopicDetail(TopicSummary):
    core_concepts: list[str]
    starter_explanation: str
    expanded_explanation: str
    analogy: str
    examples: list[str]
    practice_activity: str
    common_mistakes: list[str]
    resources: list[dict]


class CourseOverview(BaseModel):
    id: str
    title: str
    subtitle: str
    description: str
    personas: list[str]
    value_points: list[str]
    topics_count: int


class LearningRequest(BaseModel):
    topic_id: str | None = None
    topic_query: str | None = None
    proficiency_level: ProficiencyLevel = "beginner"
    learning_style: LearningStyle = "visual"
    detail_mode: DetailMode = "standard"
    include_resources: bool = True
    include_quiz: bool = True


class QuizQuestion(BaseModel):
    question: str
    options: list[str]
    explanation: str


class LearningResponse(BaseModel):
    topic_id: str
    topic_title: str
    matched_from_query: str | None = None
    focus_message: str
    sections: list[dict]
    resource_summaries: list[dict]
    quiz: list[QuizQuestion]
    next_step_prompt: str


class LearnMoreRequest(BaseModel):
    topic_id: str
    proficiency_level: ProficiencyLevel = "beginner"
    learning_style: LearningStyle = "reading"


class LearnMoreResponse(BaseModel):
    topic_id: str
    topic_title: str
    deeper_sections: list[dict]
    mini_project: str
    reflection_questions: list[str]


class QuizSubmission(BaseModel):
    topic_id: str
    answers: list[int] = Field(default_factory=list)


class QuizResult(BaseModel):
    topic_id: str
    total_questions: int
    correct_answers: int
    score_percent: float
    feedback: str
    reviewed_questions: list[dict]


class FeedbackCreate(BaseModel):
    learner_name: str = "Anonymous"
    topic_id: str
    proficiency_level: ProficiencyLevel
    learning_style: LearningStyle
    detail_mode: DetailMode
    rating: int = Field(ge=1, le=5)
    quiz_score: float = Field(ge=0, le=100)
    comment: str = ""


class FeedbackResponse(BaseModel):
    message: str
    id: int


class FeedbackRecord(BaseModel):
    learner_name: str
    topic_id: str
    proficiency_level: str
    learning_style: str
    detail_mode: str
    rating: int
    quiz_score: float
    comment: str
    created_at: datetime


class DashboardMetrics(BaseModel):
    total_feedback_entries: int
    average_rating: float
    average_quiz_score: float
    most_requested_topics: list[dict]
    recent_feedback: list[FeedbackRecord]


class RegisterRequest(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    email: str
    password: str = Field(min_length=6, max_length=128)


class LoginRequest(BaseModel):
    email: str
    password: str = Field(min_length=6, max_length=128)


class UserProfile(BaseModel):
    id: int
    full_name: str
    email: str
    created_at: datetime


class AuthResponse(BaseModel):
    token: str
    user: UserProfile


class MessageResponse(BaseModel):
    message: str


class ActivityRecord(BaseModel):
    id: int
    topic_id: str
    topic_title: str
    activity_type: str
    score: float | None = None
    detail: str = ""
    description: str = ""
    created_at: datetime


class TopicReadRequest(BaseModel):
    topic_id: str
    topic_title: str | None = None


class TopicReadResponse(BaseModel):
    message: str
    topic_id: str
    topic_title: str
    already_marked: bool = False


class LearnerOverview(BaseModel):
    full_name: str
    progress_percent: float
    topics_started: int
    topics_learned: int
    quizzes_completed: int
    average_quiz_score: float
    completed_topics: int
    completed_topic_ids: list[str]
    recent_activity: list[ActivityRecord]