# config.py

# 📩 Email credentials
EMAIL_USER = "sendo@jmsfagribusiness.com"
EMAIL_PASS = "@PPpassword"  # not app password, just the actual password

# 📥 Incoming (IMAP) server settings
EMAIL_HOST = "mail.jmsfagribusiness.com"
EMAIL_PORT = 993

# 📤 Outgoing (SMTP) server settings
SMTP_HOST = "server359.web-hosting.com"
SMTP_PORT = 465

# 🗃️ SQLite database path
# DB_PATH = "./submissions.db"

#what i touched
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "submissions.db")

