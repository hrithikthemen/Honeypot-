# Python SSH Honeypot

A lightweight Python-based Honeypot designed to simulate an SSH service and capture unauthorized login attempts. This project helps in monitoring attacker behavior, logging malicious activity, and sending real-time email alerts for suspicious login attempts.

---

## Project Overview

This Honeypot mimics a fake SSH server running on a custom port (default: 2222).
When an attacker attempts to connect and enter credentials:

* The connection is logged
* Username and password attempts are captured
* The activity is stored in log files
* An email alert is sent instantly to the administrator

This allows security researchers and students to observe attack patterns safely without exposing real infrastructure.

---

## Features

* Simulates SSH login service
* Logs all login attempts
* Sends real-time email alerts
* Automatically creates log directory
* Lightweight and easy to deploy
* Helps analyze attacker behavior

---

## Tech Stack

* Python 3
* Socket Programming
* Logging Module
* SMTP (Email Alerts)

---

## Dependencies

This project uses the following Python libraries:

### Built-in Libraries (No Installation Required)

* `socket` – For network communication
* `os` – For directory management
* `logging` – For activity logging
* `smtplib` – For sending email alerts
* `email.message` – For formatting email content

These libraries come pre-installed with Python#, so no additional installation is required.

---

## Project Structure

```
Honeypot/
│
├── logs/
│   └── activity.log
│
├── honeypot.py
└── README.md
```

---

## Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Honeypot.git
cd Honeypot
```

### 2️⃣ Install Python (if not installed)

Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 3️⃣ Configure Email Settings

Inside the script, update:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_gmail_app_password"
```

If using Gmail:

* Enable 2-Step Verification
* Generate an **App Password**
* Use that App Password instead of your actual Gmail password

---

## How to Run

```bash
python honeypot.py
```

You will see:

```
Honeypot running locally on 0.0.0.0:2222...
```

---

## How It Works

1. Attacker connects to port 2222
2. Fake SSH login prompt is displayed
3. Entered credentials are captured
4. Data is logged into `logs/activity.log`
5. Email alert is sent to the admin
6. Access is denied

---

## Email Alert Example

Subject:

```
Honeypot Login Attempt
```

Body:

```
Tried login -> USERNAME: admin, PASSWORD: 123456 from 192.168.1.10
```

---

## 📜 Log Example

```
2026-02-06 12:45:33 Connection from ('192.168.1.10', 50422)
2026-02-06 12:45:35 Tried login -> USERNAME: root, PASSWORD: toor
```

---

## Disclaimer

This project is for **educational and research purposes only**.
Do not deploy it in production environments without proper security controls.

---
