# Work Time Manager Pro(WTM)

A professional Django-based web application for tracking employee work hours, managing projects across global regions, and automated invoicing.

> **Live Demo (AWS):** [http://51.21.102.103:8000](http://51.21.102.103:8000)

## Features
- Project Management: Full CRUD with unique job numbers and regional prefix validation (EMEA, APAC, NA, LATAM).

- Time Tracking: Daily work logging with task descriptions, hours, and automated rate calculations.

- Invoicing System: Generate and manage invoices with automated status tracking.

-  Notifications: Integrated Celery & Redis for background email notifications.

- Advanced Auth: Role-based access control and employee profile management.

- Dashboard: Real-time workload statistics and project overview.

## Tech Stack
- **Framework:** Django 6.0.3
- **Database:** PostgreSQL 15
- **Task Queue:** Celery + Redis 7
- **Containerization:** Docker & Docker Compose
- **Infrastructure:** [AWS EC2 Deployment](http://51.21.102.103:8000)
- **Frontend:** Bootstrap 5
- 
## Deployment (Docker)

The application is fully containerized for consistent behavior across environments.

1. Prerequisites
- Docker & Docker Compose installed.

- A .env file configured in the root directory.

2. Quick Start (Production/Staging)
```bash

git clone https://github.com/vyankov84/work_time_manager.git
cd work_time_manager

# Build and start all services (App, DB, Redis)
docker compose up -d --build

# Run migrations within the container
docker compose exec web python manage.py migrate

# Create your admin account
docker compose exec web python manage.py createsuperuser
```
3. Environment Variables (.env)

DEBUG=False
SECRET_KEY='your-secure-key'
ALLOWED_HOSTS=your-aws-ip,localhost

DB_NAME=work_time_pro
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0

## Local Development (Traditional)
1. Create venv: python -m venv venv
2. Activate venv: source venv/bin/activate (or venv\Scripts\activate on Windows)
3. Install: pip install -r requirements.txt
4. Run: python manage.py runserver

