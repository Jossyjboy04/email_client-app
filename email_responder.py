# email_responder.py

import smtplib
from email.message import EmailMessage
from config import EMAIL_USER, EMAIL_PASS, SMTP_HOST, SMTP_PORT

def _send_email(to_email, subject, body):
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = to_email
        msg.set_content(body)

        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)

        print(f"📤 Email sent to {to_email}: {subject}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

def send_success_reply(to_email, name="there"):
    subject = "✅ Submission Received"
    body = (
        f"Hello {name},\n\n"
        "Your data submission has been received and processed successfully.\n\n"
        "Thank you!\n- The Halo Server Team"
    )
    _send_email(to_email, subject, body)

def send_invalid_format_reply(to_email, name="there"):
    subject = "⚠️ Invalid Format Detected"
    body = (
        f"Hello {name},\n\n"
        "We received your email, but the format of your data was incorrect.\n"
        "Please submit your data in the following format:\n"
        "temperature: 23\nstatus: OK\n\n"
        "Let us know if you need help.\n\n- The Halo Server Team"
    )
    _send_email(to_email, subject, body)

def send_unknown_user_reply(to_email, name="there"):
    subject = "❗ Unrecognized Sender"
    body = (
        f"Hello {name},\n\n"
        "We couldn't find your record in our database. Please ensure you're registered "
        "before submitting data.\n\nThanks,\n- The Halo Server Team"
    )
    _send_email(to_email, subject, body)
