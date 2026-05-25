import os

# HEAVY DRIFT — 7 vars missing from all config files
# Developer adds OAuth + payments + Redis but forgets to update configs

GOOGLE_CLIENT_ID     = os.getenv("GOOGLE_CLIENT_ID")                          # critical
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")                      # critical
REDIS_URL            = os.getenv("REDIS_URL")                                 # critical
STRIPE_API_KEY       = os.getenv("STRIPE_API_KEY")                            # critical
STRIPE_WEBHOOK_SEC   = os.getenv("STRIPE_WEBHOOK_SECRET")                     # critical
JWT_REFRESH_SECRET   = os.getenv("JWT_REFRESH_SECRET")                        # critical
OAUTH_REDIRECT_URI   = os.getenv("OAUTH_REDIRECT_URI", "http://localhost/cb") # warning

def google_login_url():
    return f"https://accounts.google.com/auth?client_id={GOOGLE_CLIENT_ID}"
