# Simulated in-memory notification store
user_notification_store = {}

# Simulate processing a notification
def process_notification(notification):
    user_id = notification.user_id
    message = f"{notification.type.upper()} → {notification.message}"

    if user_id not in user_notification_store:
        user_notification_store[user_id] = []
    user_notification_store[user_id].append(message)

# Simulate fetching notifications
def get_notifications_for_user(user_id: int):
    return user_notification_store.get(user_id)
