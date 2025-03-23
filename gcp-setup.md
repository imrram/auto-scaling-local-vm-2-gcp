gcloud compute instances create cloud-vm \
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