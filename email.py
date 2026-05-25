import os

# MEDIUM DRIFT — 4 vars missing from all config files
# Developer adds email verification but forgets to update configs

SMTP_HOST     = os.getenv("SMTP_HOST")             # critical — no default
SMTP_USER     = os.getenv("SMTP_USER")             # critical — no default
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")         # critical — no default
SMTP_PORT     = os.getenv("SMTP_PORT", "587")      # warning  — has default

def send_email(to, subject, body):
    print(f"Sending email via {SMTP_HOST}:{SMTP_PORT}")
