import os

# LOW DRIFT — 2 vars missing from all config files
# Developer adds monitoring/logging but forgets to update configs

SENTRY_DSN = os.getenv("SENTRY_DSN")              # critical  — no default
LOG_LEVEL  = os.getenv("LOG_LEVEL", "INFO")       # warning   — has default

def init_monitoring():
    print(f"Monitoring started | DSN: {SENTRY_DSN} | Level: {LOG_LEVEL}")
