from fastapi import APIRouter

from app.schemas import CourseOverview, TopicDetail, TopicSummary
from app.services.content_service import TOPIC_MAP, get_course_overview, list_topics

router = APIRouter(prefix="/course", tags=["Course"])


@router.get("/overview", response_model=CourseOverview)
def course_overview():
    return get_course_overview()


@router.get("/topics", response_model=list[TopicSummary])
def course_topics():
    return list_topics()


@router.get("/topics/{topic_id}", response_model=TopicDetail)
def course_topic_detail(topic_id: str):
    return TOPIC_MAP[topic_id]
