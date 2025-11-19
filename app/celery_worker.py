from celery import Celery
from app.config import REDIS_BROKER_URL

celery_app = Celery(
    "notification_service",
    broker=REDIS_BROKER_URL,
    backend=REDIS_BROKER_URL
)

celery_app.conf.task_routes = {
    "app.tasks.*": {"queue": "notifications"}
}
