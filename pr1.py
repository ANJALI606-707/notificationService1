from fastapi import FastAPI
from pydantic import BaseModel
from queue.tasks import send_notification_task

app = FastAPI()

class NotificationRequest(BaseModel):
    user_id: str
    type: str
    message: str

@app.post("/notifications")
def send_notification(req: NotificationRequest):
    send_notification_task.delay(req.user_id, req.type, req.message)
    return {"status": "queued"}

@app.get("/users/{user_id}/notifications")
def get_notifications(user_id: str):
    # temporary: return from memory or mock
    return {"user_id": user_id, "notifications": ["Welcome!"]}

from celery import Celery
from app.services import email, sms, inapp

celery_app = Celery("notifier", broker="redis://localhost:6379/0")

@celery_app.task(bind=True, max_retries=3)
def send_notification_task(self, user_id, notif_type, message):
    try:
        if notif_type == "email":
            email.send(user_id, message)
        elif notif_type == "sms":
            sms.send(user_id, message)
        elif notif_type == "inapp":
            inapp.store(user_id, message)
        else:
            raise ValueError("Invalid notification type")
    except Exception as e:
        raise self.retry(exc=e, countdown=5)

notifications = {}  # Replace with DB later

def store(user_id, message):
    if user_id not in notifications:
        notifications[user_id] = []
    notifications[user_id].append(message)

def send(user_id, message):
    print(f"Sending EMAIL to {user_id}: {message}")

def send(user_id, message):
    print(f"Sending SMS to {user_id}: {message}")
