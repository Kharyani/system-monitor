import psutil
import time
import csv
from datetime import datetime

CPU_THRESHOLD = 80
RAM_THRESHOLD = 80
DISK_THRESHOLD = 80

log_file = "system_logs.csv"


# ---------------------------
# Initialize log file
# ---------------------------
def init_log():
    with open(log_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "CPU", "RAM", "Disk"])


# ---------------------------
# Get system stats
# ---------------------------
def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, ram, disk


# ---------------------------
# Log data
# ---------------------------
def log_data(cpu, ram, disk):
    with open(log_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), cpu, ram, disk])


# ---------------------------
# Monitoring function
# ---------------------------
def start_monitoring():
    print("\n📊 Monitoring Started (Press Ctrl+C to stop)\n")

    try:
        while True:
            cpu, ram, disk = get_stats()

            print(f"CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

            # Alerts
            if cpu > CPU_THRESHOLD:
                print("⚠️ ALERT: High CPU Usage!")

            if ram > RAM_THRESHOLD:
                print("⚠️ ALERT: High RAM Usage!")

            if disk > DISK_THRESHOLD:
                print("⚠️ ALERT: High Disk Usage!")

            log_data(cpu, ram, disk)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n🛑 Monitoring Stopped")


# ---------------------------
# View logs
# ---------------------------
def view_logs():
    try:
        with open(log_file, "r") as file:
            print("\n📄 SYSTEM LOGS:\n")
            print(file.read())
    except FileNotFoundError:
        print("No logs found.")


# ---------------------------
# Set thresholds
# ---------------------------
def set_thresholds():
    global CPU_THRESHOLD, RAM_THRESHOLD, DISK_THRESHOLD

    CPU_THRESHOLD = int(input("Set CPU threshold: "))
    RAM_THRESHOLD = int(input("Set RAM threshold: "))
    DISK_THRESHOLD = int(input("Set Disk threshold: "))

    print("✅ Thresholds updated!")


# ---------------------------
# MENU SYSTEM
# ---------------------------
def menu():
    init_log()

    while True:
        print("\n===== SYSTEM MONITOR =====")
        print("1. Start Monitoring")
        print("2. Set Thresholds")
        print("3. View Logs")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            start_monitoring()

        elif choice == "2":
            set_thresholds()

        elif choice == "3":
            view_logs()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


# Run program
menu()