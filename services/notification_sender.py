from models import Notification

# Simulate sending to a queue (RabbitMQ/Kafka simulation)
def send_notification_to_queue(notification: Notification):
    # In real-world, push to RabbitMQ or Kafka here
    print(f"Pushed to queue: {notification}")
