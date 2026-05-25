import os
from flask import Flask, jsonify

app = Flask(__name__)

# Phase 1 env vars — declared in all config files (no drift)
DATABASE_URL = os.getenv("DATABASE_URL")   # critical
SECRET_KEY   = os.getenv("SECRET_KEY")    # critical

@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "1.0"})

@app.route("/")
def home():
    return jsonify({"message": "Auth Service is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
