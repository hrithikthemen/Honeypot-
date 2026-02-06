import socket
import os
import logging
import smtplib
from email.message import EmailMessage

# === Email Setup ===
EMAIL_ADDRESS = 
EMAIL_PASSWORD = "asvi mcyz xhdv uuxq"  # Use Gmail App Password if 2FA is on

def send_email_alert(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS  # You can add more recipients

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print(f"[!] Failed to send email: {e}")
        logger.error(f"Failed to send email: {e}")

# === Logging Setup ===
if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger("honeypot")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("logs/activity.log")
    formatter = logging.Formatter("%(asctime)s %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# === Honeypot Start ===
def start_honeypot(host="0.0.0.0", port=2222):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)
        print(f"🍯 Honeypot running locally on {host}:{port}... (press Ctrl+C to stop)")
        logger.info(f"Honeypot started on {host}:{port}")
    except Exception as e:
        print(f"❌ Failed to start honeypot: {e}")
        logger.error(f"Failed to start honeypot: {e}")
        return

    while True:
        try:
            client, addr = server.accept()
            print(f"[+] Connection from {addr}")
            logger.info(f"Connection from {addr}")

            client.sendall(b"Welcome to Secure SSH!\nLogin: ")
            username = client.recv(1024).decode().strip()
            client.sendall(b"Password: ")
            password = client.recv(1024).decode().strip()

            message = f"Tried login -> USERNAME: {username}, PASSWORD: {password} from {addr[0]}"
            print(message)
            logger.info(message)

            # 📧 Send email alert
            send_email_alert("🔐 Honeypot Login Attempt", message)

            client.sendall(b"Access denied.\n")

        except Exception as e:
            print(f"[!] Error with {addr}: {e}")
            logger.error(f"Error with {addr}: {e}")
        finally:
            client.close()

if __name__ == "__main__":
    start_honeypot()