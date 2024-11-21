import re

def parse_log_line(line):
    """Parses a log line and returns a dictionary containing relevant information.

    Args:
        line: A string representing a log line.

    Returns:
        A dictionary containing the following keys:
            - timestamp: Timestamp of the log message.
            - host: Hostname.
            - program: Program that generated the log message.
            - message: Log message.
    """

    # Regular expression to extract information from the log line
    pattern = r"^(\w{3} \d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+\[\d+\]) (.*)$"
    match = re.match(pattern, line)

    if match:
        timestamp, host, program, message = match.groups()
        return {
            "timestamp": timestamp,
            "host": host,
            "program": program,
            "message": message
        }
    else:
        return None

def parse_log_file(filename):
    """Parses a log file and returns a list of dictionaries, each representing a log line.

    Args:
        filename: The name of the log file.

    Returns:
        A list of dictionaries, each containing information about a log line.
    """

    logs = []
    with open(filename, 'r') as f:
        for line in f:
            log_info = parse_log_line(line)
            if log_info:
                logs.append(log_info)

    return logs

# Example usage:
filename = "your_log_file.log"
log_data = parse_log_file(filename)

for log in log_data:
    print(log)