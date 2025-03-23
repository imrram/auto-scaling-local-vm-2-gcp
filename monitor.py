import psutil
import os

cpu_threshold = 75  # 75%
mem_threshold = 75  # 75%

# Check CPU and Memory
cpu_usage = psutil.cpu_percent(interval=1)
mem_usage = psutil.virtual_memory().percent

if cpu_usage > cpu_threshold or mem_usage > mem_threshold:
    print("Resource usage exceeded! Triggering GCP scaling...")
    # Trigger GCP instance creation (replace with your project ID and zone)
    os.system("gcloud compute instances create cloud-vm --image-family ubuntu-2204-lts --image-project ubuntu-os-cloud --zone us-central1-a")