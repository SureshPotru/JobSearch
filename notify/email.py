import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "YOUR_EMAIL"
PASSWORD = "APP_PASSWORD"

def send_email(jobs):
    if not jobs:
        return

    body = ""
    for j in jobs:
        body += f"""
{j['title']} – {j['company']}
Location: {j['location']}
Score: {j['score']}
Apply: {j['url']}

-------------------------
"""

    msg = MIMEText(body)
    msg["Subject"] = "🚀 New Senior DevOps Jobs – Hyderabad"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as s:
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(msg)
