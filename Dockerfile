FROM python:3.11-slim

# Avoid writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "smart_feedback.wsgi:application", "--bind", "0.0.0.0:8000"]
