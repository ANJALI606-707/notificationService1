from fastapi import FastAPI, HTTPException
from models import Notification, UserNotifications
from services.notification_sender import send_notification_to_queue
from queue.tasks import get_notifications_for_user

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr

app = FastAPI()

# Send a notification (POST /notifications)
@app.post("/notifications")
def send_notification(notification: Notification):
    send_notification_to_queue(notification)
    return {"message": "Notification sent to queue"}

# Get user notifications (GET /users/{id}/notifications)
@app.get("/users/{user_id}/notifications", response_model=UserNotifications)
def get_user_notifications(user_id: int):
    notifications = get_notifications_for_user(user_id)
    if notifications is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "notification": notifications}
