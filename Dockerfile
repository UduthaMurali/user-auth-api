FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Phase 1 — original vars
ENV DATABASE_URL=""
ENV SECRET_KEY=""

# Phase 2 — monitoring vars (added after drift was detected)
ENV SENTRY_DSN=""
ENV LOG_LEVEL="INFO"

# Phase 3 — email vars (added after drift was detected)
ENV SMTP_HOST=""
ENV SMTP_PORT="587"
ENV SMTP_USER=""
ENV SMTP_PASSWORD=""

# Phase 4 — OAuth + payments vars (added after drift was detected)
ENV GOOGLE_CLIENT_ID=""
ENV GOOGLE_CLIENT_SECRET=""
ENV GOOGLE_REDIRECT_URI=""
ENV REDIS_URL=""
ENV STRIPE_API_KEY=""
ENV STRIPE_WEBHOOK_SECRET=""
ENV JWT_REFRESH_SECRET=""

EXPOSE 5000
CMD ["python", "app.py"]
