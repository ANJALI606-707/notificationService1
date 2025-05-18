# notificationService1
Notification Service: Objective: Built a system to send notifications to users.

# FastAPI Task Manager

A simple FastAPI-based backend for user and task management using Pydantic for data validation.

## Features

- User registration & task routes
- Pydantic models and validation
- Environment variable support

## Setup

```bash
python -m venv venv
venv\Scripts\activate         # Use Activate.ps1 with execution policy bypass if needed
pip install -r requirements.txt
pip install email-validator   # Required for Pydantic email validation
uvicorn main:app --reload
