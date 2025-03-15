import smtplib
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
port = 587
sender_email = input("Enter sender email address and press enter: ")
receiver_email = input("Enter receiver email address and press enter: ")
message = input("Write your message and press enter: ")

msg = MIMEText(message)
msg['Subject'] = "Automated Email"
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        password = input("Enter sender email app password: ")
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
    print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Error: {e}")