import random
import csv
import time
from datetime import datetime

LOG_FILE = r"D:\log-analytics-monitoring-engine\backend\sample_log\data_log.log"

log_levels = ["INFO", "ERROR", "WARN", "DEBUG"]
log_weights = [0.7, 0.1, 0.15, 0.05]

services = ["auth", "payment", "inventory", "shipping", "user", "orders", "notifications", "analytics", "search", "recommendation"]

info_msgs = ["Request processed successfully", "User logged in", "Data retrieved", "Operation completed",
             "Cache hit", "Cache list", "Connection established", "Transaction completed", "Email sent", "Notification delivered"]
error_msgs = ["Database connection failed", "Timeout occurred", "Null pointer exception", "Out of memory",
              "Service unavailable", "Failed to process request", "Unauthorized access attempt",
              "Data validation error", "Disk full", "API rate limit exceeded"]

# Write header once, separately
with open(LOG_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "service", "log_level", "message"])

print("Generating log data...")

while True:
    level = random.choices(log_levels, weights=log_weights)[0]

    if level == "ERROR":
        message = random.choice(error_msgs)
    else:
        message = random.choice(info_msgs)

    row = [
        datetime.now().isoformat(),
        random.choice(services),  
        level,                  
        message                   
    ]

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    time.sleep(0.5) 