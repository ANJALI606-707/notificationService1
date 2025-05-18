from pydantic import BaseModel, EmailStr
from typing import List

class Notification(BaseModel):
    user_id: int
    type: str  # "email", "sms", "in-app"
    message: str
    email: EmailStr | None = None
    phone: str | None = None

class UserNotifications(BaseModel):
    user_id: int
    notifications: List[str]
