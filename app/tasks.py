from app.celery_worker import celery_app
from app.email_utils import send_email

@celery_app.task(name="app.tasks.send_email_task")
def send_email_task(to_email: str, subject: str, message: str):
    send_email(to_email, subject, message)
