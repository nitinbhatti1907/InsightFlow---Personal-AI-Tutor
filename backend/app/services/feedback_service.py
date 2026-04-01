from collections import Counter

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import LearnerFeedback, User


def create_feedback(db: Session, payload, user: User | None = None) -> LearnerFeedback:
    feedback_payload = payload.model_dump()
    if user:
        feedback_payload["learner_name"] = user.full_name
        feedback_payload["user_id"] = user.id
    feedback = LearnerFeedback(**feedback_payload)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return feedback


def build_dashboard_metrics(db: Session) -> dict:
    feedback_items = list(db.scalars(select(LearnerFeedback).order_by(LearnerFeedback.created_at.desc())))
    total = len(feedback_items)

    average_rating = round(sum(item.rating for item in feedback_items) / total, 2) if total else 0.0
    average_quiz_score = round(sum(item.quiz_score for item in feedback_items) / total, 2) if total else 0.0

    counter = Counter(item.topic_id for item in feedback_items)
    most_requested_topics = [
        {"topic_id": topic_id, "requests": count}
        for topic_id, count in counter.most_common(5)
    ]

    recent_feedback = [
        {
            "learner_name": item.learner_name,
            "topic_id": item.topic_id,
            "proficiency_level": item.proficiency_level,
            "learning_style": item.learning_style,
            "detail_mode": item.detail_mode,
            "rating": item.rating,
            "quiz_score": item.quiz_score,
            "comment": item.comment,
            "created_at": item.created_at,
        }
        for item in feedback_items[:8]
    ]

    return {
        "total_feedback_entries": total,
        "average_rating": average_rating,
        "average_quiz_score": average_quiz_score,
        "most_requested_topics": most_requested_topics,
        "recent_feedback": recent_feedback,
    }
