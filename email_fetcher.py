# email_fetcher.py

import imaplib
import email
from email.header import decode_header
from config import EMAIL_USER, EMAIL_PASS, EMAIL_HOST, EMAIL_PORT
from data_parser import extract_key_values
from db_handler import (
    save_key_values,
    email_exists_in_users,
    is_email_processed,
    mark_email_as_processed,
    get_user_name,
)
from email_responder import (
    send_success_reply,
    send_unknown_user_reply,
    send_invalid_format_reply,
)

def connect_and_process_emails():
    try:
        mail = imaplib.IMAP4_SSL(EMAIL_HOST, EMAIL_PORT)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        result, data = mail.search(None, "UNSEEN")
        email_ids = data[0].split()

        if not email_ids:
            print("📭 No new unread emails.")
            return

        for eid in email_ids:
            result, msg_data = mail.fetch(eid, "(RFC822)")
            if result != "OK":
                print(f"❌ Failed to fetch email with ID {eid}")
                continue

            msg = email.message_from_bytes(msg_data[0][1])
            subject = decode_str(msg["Subject"])
            from_email = decode_str(msg.get("From")).split("<")[-1].replace(">", "").strip()
            message_id = msg.get("Message-ID", "")

            if is_email_processed(message_id):
                continue  # Skip already processed emails

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        charset = part.get_content_charset() or "utf-8"
                        body = part.get_payload(decode=True).decode(charset, errors="replace")
                        break
            else:
                charset = msg.get_content_charset() or "utf-8"
                body = msg.get_payload(decode=True).decode(charset, errors="replace")

            body = body.strip()
            print(f"📨 Processing email from: {from_email}")

            # Check if sender exists in user database
            if email_exists_in_users(from_email):
                name = get_user_name(from_email)
                data = extract_key_values(body)
                if data:
                    save_key_values(from_email, data)
                    send_success_reply(from_email, name)
                else:
                    send_invalid_format_reply(from_email, name)
            else:
                name = extract_name_from_body_or_default(body)
                send_unknown_user_reply(from_email, name)

            mark_email_as_processed(message_id)

        mail.logout()

    except Exception as e:
        print(f"❌ Error during email fetching: {e}")

def decode_str(s):
    if not s:
        return ""
    decoded_parts = decode_header(s)
    decoded_string = ""
    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            decoded_string += part.decode(encoding or "utf-8", errors="replace")
        else:
            decoded_string += part
    return decoded_string

def extract_name_from_body_or_default(body):
    for line in body.splitlines():  
        if "name" in line.lower():
            return line.split(":")[-1].strip().title()
    return "there"
