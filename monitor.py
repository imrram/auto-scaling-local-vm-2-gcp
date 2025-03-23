import psutil
import os
import time
import subprocess

cpu_threshold = 75  # 75%
mem_threshold = 75  # 75%

while True:
    # Check CPU and Memory
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu_usage}%, Memory Usage: {mem_usage}%")  # Debugging output

    if cpu_usage > cpu_threshold or mem_usage > mem_threshold:
        print("Resource usage exceeded! Triggering GCP scaling...")
        try:
            # Trigger GCP instance creation with a startup script
            subprocess.run([
                "gcloud", "compute", "instances", "create", "cloud-vm",
                "--image-family", "ubuntu-2204-lts",
                "--image-project", "ubuntu-os-cloud",
                "--zone", "us-central1-a",
                "--metadata", "startup-script=#! /bin/bash\n"
                              "apt update && apt install -y python3-pip\n"
                              "pip3 install flask\n"
                              "echo 'from flask import Flask\n"
                              "app = Flask(__name__)\n"
                              "@app.route(\"/\")\n"
                              "def home():\n"
                              "    return \"Hello from GCP!\"\n"
                              "if __name__ == \"__main__\":\n"
                              "    app.run(host=\"0.0.0.0\", port=5000)' > /app.py\n"
                              "python3 /app.py"
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to create GCP instance: {e}")
    
    time.sleep(60)  # Check every 60