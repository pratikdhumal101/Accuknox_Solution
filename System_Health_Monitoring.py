import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Define thresholds
cpu_threshold = int(input("Enter the CPU Threshold:"))  # CPU usage threshold in percent
memory_threshold = int(input("Enter the Memory Threshold:"))  # Memory usage threshold in percent
disk_threshold = int(input("Enter the disk Threshold:"))  # Disk usage threshold in percent

# Check CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > cpu_threshold:
    logging.warning(f"High CPU usage detected: {cpu_usage}%")

# Check memory usage
memory_usage = psutil.virtual_memory().percent
if memory_usage > memory_threshold:
    logging.warning(f"High memory usage detected: {memory_usage}%")

# Check disk usage
disk_usage = psutil.disk_usage('/').percent
if disk_usage > disk_threshold:
    logging.warning(f"High disk usage detected: {disk_usage}%")

# Check running processes
# Get the number of running processes
running_processes = sum(1 for _ in psutil.process_iter())

logging.info(f"Number of running processes: {running_processes}")

# Print system information
print("System Health Report:")
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"Disk Usage: {disk_usage}%")
print(f"Number of Running Processes: {running_processes}")

