from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import (
    DashboardMetrics,
    FeedbackCreate,
    FeedbackResponse,
    LearnerOverview,
    LearnMoreRequest,
    LearnMoreResponse,
    LearningRequest,
    LearningResponse,
    QuizResult,
    QuizSubmission,
    TopicReadRequest,
    TopicReadResponse,
)
from app.services.activity_service import (
    build_learner_overview,
    log_activity,
    mark_topic_as_read,
)
from app.services.auth_service import get_current_user
from app.services.content_service import (
    generate_learn_more,
    generate_learning_content,
    resolve_topic_title,
)
from app.services.feedback_service import build_dashboard_metrics, create_feedback
from app.services.quiz_service import evaluate_quiz

router = APIRouter(prefix="/learning", tags=["Learning"])


@router.post("/generate", response_model=LearningResponse)
def generate_content(
    payload: LearningRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    try:
        response = generate_learning_content(**payload.model_dump())
        log_activity(
            db,
            user,
            topic_id=response["topic_id"],
            topic_title=response["topic_title"],
            activity_type="generate",
            detail=f"Generated content for {response['topic_title']}",
        )
        return response
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post("/learn-more", response_model=LearnMoreResponse)
def learn_more(
    payload: LearnMoreRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    response = generate_learn_more(**payload.model_dump())
    log_activity(
        db,
        user,
        topic_id=response["topic_id"],
        topic_title=response["topic_title"],
        activity_type="learn_more",
        detail=f"Opened Learn More for {response['topic_title']}",
    )
    return response


@router.post("/evaluate-quiz", response_model=QuizResult)
def evaluate(
    payload: QuizSubmission,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    result = evaluate_quiz(**payload.model_dump())
    topic_title = resolve_topic_title(result["topic_id"])
    log_activity(
        db,
        user,
        topic_id=result["topic_id"],
        topic_title=topic_title,
        activity_type="quiz",
        detail=f"Completed quiz for {topic_title}",
        score=result["score_percent"],
    )
    return result


@router.post("/mark-read", response_model=TopicReadResponse)
def mark_read(
    payload: TopicReadRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return mark_topic_as_read(
        db,
        user,
        topic_id=payload.topic_id,
        topic_title=payload.topic_title,
    )


@router.post("/feedback", response_model=FeedbackResponse)
def submit_feedback(
    payload: FeedbackCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    feedback = create_feedback(db, payload, user=user)
    return {"message": "Feedback saved successfully.", "id": feedback.id}


@router.get("/dashboard", response_model=DashboardMetrics)
def dashboard(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return build_dashboard_metrics(db)


@router.get("/my-overview", response_model=LearnerOverview)
def my_overview(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return build_learner_overview(db, user)