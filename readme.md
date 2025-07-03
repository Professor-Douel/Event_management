# Name of the project

This project is a Django-based REST API for managing events such as conferences, meetups, and more. It supports event CRUD operations, user registration and authentication, event registrations, and email notifications upon registration. API documentation is provided via **drf-spectacular**. The project is containerized with Docker and uses MailHog for local email testing. The database is SQLite3.

---

## Features

- Event model with fields: title, description, date, location, organizer
- CRUD operations for events via REST API
- User registration and authentication via Djoser
- Event registration endpoint
- Email notifications on event registration (via SMTP MailHog)
- API schema and interactive docs with drf-spectacular (Swagger UI)
- Dockerized with `docker-compose`
- Uses SQLite3 as database

---

## Requirements

- Docker & Docker Compose installed
- Python 3.11+ (for local development)
- `docker-compose` v1.27+ recommended

---

## Installing

### Instructions for launching locally:

1. Clone repository:
    ```bash
    git clone https://github.com/Professor-Douel/Event_management.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run Django server:
    ```bash
    python manage.py runserver
    ```
4. "[127.0.0.1:8000](Event_management/urls.py)" show Browsable API

---

### Instructions for launching in Docker:

1. Clone repository:
    ```bash
    git clone https://github.com/Professor-Douel/Event_management.git
    ```
2. Build & start containers:
    ```bash
    docker-compose up --build
    ```
3. Access the services:
    ```
    API server: "http://localhost:8000"

    API docs (Swagger UI): "http://localhost:8000/api/docs/"

    MailHog UI (email testing): "http://localhost:8025"
   ```
   
---

## API Documentation

Auto-generated OpenAPI schema and Swagger UI via drf-spectacular are available at:

    /api/docs/     # Swagger UI interactive docs

---
