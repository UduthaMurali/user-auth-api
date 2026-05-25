FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Phase 1: all env vars declared here
ENV DATABASE_URL=""
ENV SECRET_KEY=""

EXPOSE 5000
CMD ["python", "app.py"]
