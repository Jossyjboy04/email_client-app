# # main.py
# import time
# from datetime import datetime
# from db_handler import init_db, save_key_values
# from data_parser import extract_key_values
# from email_fetcher import connect_and_process_emails

# def main():
#     print(f"[{datetime.now()}] 🚀 Starting Halo Email Processor...")
#     init_db()
#     connect_and_process_emails()

# if __name__ == "__main__":
#     main()
import time
from db_handler import init_db, save_key_values
from data_parser import extract_key_values
from email_fetcher import connect_and_process_emails

def main():
    print("🚀 Starting Halo Email Processor...")
    init_db()

    while True:
         connect_and_process_emails()
         time.sleep(30)  # Wait 30 seconds before checking again

if __name__ == "__main__":
    main()


