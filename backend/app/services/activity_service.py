from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import LearningActivity, User
from app.seed_data import TOPICS

TOPIC_TITLES = {item["id"]: item["title"] for item in TOPICS}
TOTAL_PROGRESS_STEPS = max(len(TOPIC_TITLES), 1)


def log_activity(
    db: Session,
    user: User,
    topic_id: str,
    topic_title: str,
    activity_type: str,
    detail: str = "",
    score: float | None = None,
) -> LearningActivity:
    activity = LearningActivity(
        user_id=user.id,
        topic_id=topic_id,
        topic_title=topic_title,
        activity_type=activity_type,
        detail=detail,
        score=score,
    )
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity


def _resolve_topic_title_from_history(db: Session, user: User, topic_id: str) -> str | None:
    activity = db.scalar(
        select(LearningActivity)
        .where(
            LearningActivity.user_id == user.id,
            LearningActivity.topic_id == topic_id,
        )
        .order_by(LearningActivity.created_at.desc())
    )
    return activity.topic_title if activity else None


def mark_topic_as_read(
    db: Session,
    user: User,
    topic_id: str,
    topic_title: str | None = None,
) -> dict:
    existing = db.scalar(
        select(LearningActivity).where(
            LearningActivity.user_id == user.id,
            LearningActivity.topic_id == topic_id,
            LearningActivity.activity_type == "mark_read",
        )
    )

    resolved_title = (
        topic_title
        or TOPIC_TITLES.get(topic_id)
        or _resolve_topic_title_from_history(db, user, topic_id)
        or topic_id.replace("-", " ").title()
    )

    if existing:
        return {
            "message": f"{resolved_title} is already marked as read.",
            "topic_id": topic_id,
            "topic_title": resolved_title,
            "already_marked": True,
        }

    log_activity(
        db,
        user,
        topic_id=topic_id,
        topic_title=resolved_title,
        activity_type="mark_read",
        detail=f"Marked {resolved_title} as read",
    )

    return {
        "message": f"{resolved_title} has been marked as read and added to your progress.",
        "topic_id": topic_id,
        "topic_title": resolved_title,
        "already_marked": False,
    }


def build_learner_overview(db: Session, user: User) -> dict:
    activities = list(
        db.scalars(
            select(LearningActivity)
            .where(LearningActivity.user_id == user.id)
            .order_by(LearningActivity.created_at.desc())
        )
    )

    topics_started_ids = sorted(
        {
            item.topic_id
            for item in activities
            if item.activity_type in {"generate", "learn_more", "quiz", "mark_read"}
        }
    )

    quizzes = [item for item in activities if item.activity_type == "quiz"]

    passed_quiz_topic_ids = {
        item.topic_id for item in quizzes if (item.score or 0) >= 60
    }
    read_topic_ids = {
        item.topic_id for item in activities if item.activity_type == "mark_read"
    }

    completed_topic_ids = sorted(read_topic_ids | passed_quiz_topic_ids)

    average_quiz_score = (
        round(sum((item.score or 0) for item in quizzes) / len(quizzes), 2)
        if quizzes
        else 0.0
    )

    progress_percent = round(
        min(len(completed_topic_ids), TOTAL_PROGRESS_STEPS)
        / TOTAL_PROGRESS_STEPS
        * 100,
        2,
    )

    recent_activity = [
        {
            "id": item.id,
            "topic_id": item.topic_id,
            "topic_title": item.topic_title,
            "activity_type": item.activity_type,
            "score": item.score,
            "detail": item.detail,
            "description": item.detail,
            "created_at": item.created_at,
        }
        for item in activities[:10]
    ]

    return {
        "full_name": user.full_name,
        "progress_percent": progress_percent,
        "topics_started": len(topics_started_ids),
        "topics_learned": len(topics_started_ids),
        "quizzes_completed": len(quizzes),
        "average_quiz_score": average_quiz_score,
        "completed_topics": len(completed_topic_ids),
        "completed_topic_ids": completed_topic_ids,
        "recent_activity": recent_activity,
    }