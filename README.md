# GCP Setup Instructions

This document provides step-by-step instructions for setting up a GCP instance to run the Flask application automatically when the instance is created.

---

## **1. Prerequisites**
- A GCP account with billing enabled.
- Google Cloud SDK installed and configured on your local machine.
- A service account with the **Compute Admin** role.

---

## **2. Create a GCP Instance with Flask Pre-Installed**

To ensure the Flask application runs without errors, we use a **startup script** to install Flask and deploy the app automatically when the GCP instance is created.

### **Startup Script**
The startup script performs the following tasks:
1. Installs `python3-pip` and `flask`.
2. Creates the Flask application (`app.py`).
3. Runs the Flask app.

Here’s the command to create the GCP instance with the startup script:

```bash
gcloud compute instances create cloud-vm \
    --image-family ubuntu-2204-lts \
    --image-project ubuntu-os-cloud \
    --zone us-central1-a \
    --metadata startup-script='#! /bin/bash
    apt update && apt install -y python3-pip
    pip3 install flask
    echo "from flask import Flask
app = Flask(__name__)
@app.route(\"/\")
def home():
    return \"Hello from GCP!\"
if __name__ == \"__main__\":
    app.run(host=\"0.0.0.0\", port=5000)" > /app.py
    python3 /app.py'