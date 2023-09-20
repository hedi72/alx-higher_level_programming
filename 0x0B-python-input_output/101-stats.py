#!/usr/bin/python3
import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")

# Function to handle keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
for line in sys.stdin:
    try:
        line = line.strip()
        parts = line.split()
        if len(parts) >= 7:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()
    except ValueError:
        pass  # Ignore lines with invalid format

# Print final metrics after processing all input
print_metrics()
