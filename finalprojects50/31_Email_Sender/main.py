# email_sender.py

import smtplib
from email.message import EmailMessage
import os

def retry(func):
    def wrapper(*args, **kwargs):
        attempts = 3
        for i in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {i+1} failed: {e}")
        print("All attempts failed.")
    return wrapper

class Email:
    def __init__(self, subject, body, sender, recipients, attachments=None):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.recipients = recipients
        self.attachments = attachments or []

    def create_message(self):
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipients)
        msg.set_content(self.body)

        for file_path in self.attachments:
            try:
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(file_path)
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
            except FileNotFoundError:
                print(f"Attachment not found: {file_path}")
        return msg

@retry
def send_email(email_obj: Email, smtp_server='smtp.gmail.com', port=587, password=''):
    msg = email_obj.create_message()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(email_obj.sender, password)
        server.send_message(msg)
        print("✅ Email sent successfully!")

def main():
    print("📧 Email Sender CLI")
    sender = input("Enter your email: ")
    password = input("Enter your password (won't be displayed): ")
    recipients = input("Enter recipient emails (comma separated): ").split(',')
    subject = input("Enter subject: ")
    body = input("Enter email body: ")
    attach = input("Attach files (comma separated paths or leave blank): ").split(',') if input("Add attachments? (y/n): ").lower() == 'y' else []

    email_obj = Email(subject, body, sender, [r.strip() for r in recipients], [a.strip() for a in attach if a])
    send_email(email_obj, password=password)

if __name__ == "__main__":
    main()

