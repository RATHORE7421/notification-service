from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from app.tasks import send_email_task

app = FastAPI(title="Notification API")

class EmailNotification(BaseModel):
    to_email: EmailStr
    subject: str
    message: str

@app.post("/notify/email")
async def notify_email(notification: EmailNotification):
    send_email_task.delay(
        notification.to_email,
        notification.subject,
        notification.message
    )
    return {"status": "queued"}
