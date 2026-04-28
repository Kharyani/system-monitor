# system-monitorSystem Resource Monitoring & Alert Script
📌 Project Description

This project is a Python-based system monitoring tool that tracks real-time performance of CPU, RAM, and Disk usage. It provides alerts when system usage exceeds defined thresholds and logs all performance data into a CSV file for later analysis.

It simulates real-world monitoring tools used in IT environments like server health monitoring systems.

⚙️ Features
🔄 Real-time system monitoring (CPU, RAM, Disk)
🚨 Alert system for high resource usage
📊 Custom threshold settings
📝 Automatic logging to CSV file
📋 CLI-based menu system
🛑 Graceful start/stop monitoring
🛠 Technologies Used
Python 3
psutil (system monitoring library)
csv module
datetime module
📦 Installation
1. Install Python

Make sure Python is installed:

python --version
2. Install required library
pip install psutil
🚀 How to Run
1. Clone or download the project
system-monitor/
2. Run the program
python monitor.py
📋 Menu Options

When you run the program, you will see:

===== SYSTEM MONITOR =====
1. Start Monitoring
2. Set Thresholds
3. View Logs
4. Exit
▶️ Option 1: Start Monitoring
Starts real-time system monitoring
Displays CPU, RAM, Disk usage
Shows alerts if limits are exceeded
⚙️ Option 2: Set Thresholds
Allows user to define limits (e.g., CPU > 80%)
📄 Option 3: View Logs
Displays stored system performance data
❌ Option 4: Exit
Closes the application
📝 Output Logs

All system data is saved in:

system_logs.csv

Example format:

Time, CPU, RAM, Disk
2026-04-28 10:10:01, 25, 45, 35
2026-04-28 10:10:03, 40, 46, 35
🚨 Alerts System

If system usage exceeds thresholds:

⚠️ ALERT: High CPU Usage!
⚠️ ALERT: High RAM Usage!
⚠️ ALERT: High Disk Usage!
📊 Future Improvements
GUI dashboard using Tkinter
Graph visualization using Matplotlib
Email alert system
Desktop notifications
Cloud-based monitoring integration
👨‍💻 Author

Student Project – System Resource Monitoring Tool
Developed using Python

🏁 Conclusion

This project demonstrates real-time system monitoring, logging, and alert management using Python, making it useful for understanding basic system administration and performance tracking.
