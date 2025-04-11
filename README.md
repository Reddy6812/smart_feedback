# smart_feedback
---

```markdown
## Running the Project

This section explains how to run the Smart Feedback Platform locally, with Docker, and use JWT for authentication. It also covers deploying via GitLab CI/CD.

---

### Local Development

1. Create and activate a virtual environment, then install requirements:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

2. Run migrations and start the Django server:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Create a superuser to access the admin dashboard
python manage.py runserver
```

---

### Celery Workers (Optional)

Start the Celery worker (in one terminal):

```bash
celery -A smart_feedback worker -l info
```

Start Celery Beat for scheduled tasks (in another terminal):

```bash
celery -A smart_feedback beat -l info
```

---

### Docker Deployment

1. Build the Docker image:

```bash
docker build -t smart-feedback-app .
```

2. Run the Docker container:

```bash
docker run -d -p 8000:8000 smart-feedback-app
```

---

### JWT Authentication

To obtain a token, send a POST request to `/api/token/` with a JSON payload:

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

To refresh the token, send a POST request to `/api/token/refresh/` with your refresh token.

Use the access token in your request headers as follows:

```
Authorization: Bearer <your_access_token>
```

---

### GitLab CI/CD

1. Commit and push your code to your GitLab repository.

2. The provided `.gitlab-ci.yml` file is configured to:

- Build the Docker image
- Push it to the GitLab container registry
- Deploy the image to your AWS EC2 instance via SSH

---
```

Let me know if you want this integrated with the full README or if you'd like a PDF/Markdown file output.
