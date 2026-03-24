import requests
import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_USER = os.getenv("EMAIL_USER")


def send_email(to_email, subject, body):

    print("🔥 SENDGRID FUNCTION STARTED")

    data = {
        "personalizations": [
            {
                "to": [{"email": to_email}],
                "subject": subject
            }
        ],
        "from": {"email": EMAIL_USER},
        "content": [
            {
                "type": "text/plain",
                "value": f"""
Hello,

Thank you for reaching out.

{body}

Best regards,
Your Company
"""
            }
        ]
    }

    response = requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={
            "Authorization": f"Bearer {SENDGRID_API_KEY}",
            "Content-Type": "application/json"
        },
        json=data
    )

    # 👇 DEBUG HERE
    print("📧 SENDGRID RESPONSE STATUS:", response.status_code)
    print("📧 SENDGRID RESPONSE BODY:", response.text)
    print("STATUS CODE:", response.status_code)

    if response.status_code == 202:
        print("✅ Email sent successfully via SendGrid")
    else:
        print("❌ SENDGRID ERROR:", response.text)


def trigger_actions(lead):
    print("🔥 TRIGGER ACTIONS CALLED")
    send_email(
        lead.email,
        "Thanks for reaching out",
        lead.response
    )