
import os
from functools import wraps
import requests
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

# ========== HARDCODED CONFIGURATION ==========
# TODO: Replace these with your actual Supabase credentials
SUPABASE_URL = "https://rcrbazstbgqfmhzubmrg.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJjcmJhenN0YmdxZm1oenVibXJnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Nzc2NTMxMiwiZXhwIjoyMDczMzQxMzEyfQ.Y42dwejCsS66t0d-cMXaxL5Gxm9YuWx1JebUQelC5FQ"
FLASK_SECRET_KEY = "your-secret-key-change-this"

app.secret_key = FLASK_SECRET_KEY
# ============================================



# ====================================

@app.route("/")
def bus_tracker():
    """Real-time bus tracker"""
    return render_template(
        "bus_tracker.html",
        supabase_url=SUPABASE_URL,
        supabase_anon_key=SUPABASE_ANON_KEY,
    )

if __name__ == "__main__":
    app.run(debug=True)
