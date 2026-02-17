# ============================================================
#  WEEK 06 LAB: NETWORK DIAGNOSTIC LOGGER
#  COMP2152
#  [Rehaan Lachporia] [101594859]
# ============================================================
#
#  This program runs network commands (ping, nslookup, ifconfig),
#  parses their output, and logs results to files.
#
#  YOUR TASKS (3 tasks — look for *** TASK *** markers):
#
#  Task 1: Complete write_to_log() and read_log()
#          — Write to a text file in append mode
#          — Read from a text file
#
#  Task 2: Complete log_to_csv() and read_csv_log()
#          — Write a row to a CSV file
#          — Read and display CSV rows
#
#  Task 3: Complete safe_read_log()
#          — Add try/except/finally for missing files
#
# ============================================================

import subprocess
import csv
from datetime import datetime


# ============================================================
#  SECTION A: Running System Commands (COMPLETE — provided)
# ============================================================

def run_ping(host):
    """Run ping -c 3 on a host and return the output."""
    result = subprocess.run(
        ["ping", "-c", "3", host],
        capture_output=True, text=True
    )
    return result.stdout


def run_nslookup(domain):
    """Run nslookup on a domain and return the output."""
    result = subprocess.run(
        ["nslookup", domain],
        capture_output=True, text=True
    )
    return result.stdout


def get_network_info():
    """Run ifconfig en0 and return the output."""
    result = subprocess.run(
        ["ifconfig", "en0"],
        capture_output=True, text=True
    )
    return result.stdout


def get_arp_table():
    """Run arp -a to show all devices on the local network."""
    result = subprocess.run(
        ["arp", "-a"],
        capture_output=True, text=True
    )
    return result.stdout


def get_hostname():
    """Run hostname to get the computer's network name."""
    result = subprocess.run(
        ["hostname"],
        capture_output=True, text=True
    )
    return result.stdout.strip()


# ============================================================
#  SECTION B: Parsing Command Output (COMPLETE — provided)
# ============================================================

def parse_ping(output):
    """Parse ping output and extract key statistics."""
    lines = output.strip().split("\n")
    stats = {
        "transmitted": 0,
        "received": 0,
        "loss": "100%",
        "avg_ms": "N/A",
        "status": "Failed"
    }

    for line in lines:
        if "packets transmitted" in line:
            parts = line.split(", ")
            stats["transmitted"] = int(parts[0].strip().split()[0])
            stats["received"] = int(parts[1].strip().split()[0])
            stats["loss"] = parts[2].strip().split()[0]

        if "round-trip" in line or "rtt" in line:
            times_part = line.split("=")[1].strip()
            times = times_part.split("/")
            stats["avg_ms"] = times[1]

    if stats["received"] > 0:
        stats["status"] = "Success"

    return stats


def parse_nslookup(output):
    """Parse nslookup output and extract the resolved IP address."""
    lines = output.strip().split("\n")
    result = {"ip": "Not found", "status": "Failed"}

    found_answer = False
    for line in lines:
        if "Non-authoritative answer" in line:
            found_answer = True
        if found_answer and "Address:" in line:
            ip = line.split("Address:")[1].strip()
            if ip and "." in ip:
                result["ip"] = ip
                result["status"] = "Success"
                break

    return result


def parse_mac_address(output):
    """Parse ifconfig output to extract MAC and IP address."""
    lines = output.strip().split("\n")
    info = {"mac": "Not found", "ip": "Not found"}

    for line in lines:
        line = line.strip()
        if line.startswith("ether"):
            info["mac"] = line.split()[1]
        if "inet " in line and "inet6" not in line:
            info["ip"] = line.split()[1]

    return info


def parse_arp_table(output):
    """Parse arp -a output and return a list of devices."""
    lines = output.strip().split("\n")
    devices = []

    for line in lines:
        if "at" in line and "on" in line:
            parts = line.split()
            ip = "unknown"
            mac = "unknown"
            for part in parts:
                if part.startswith("(") and part.endswith(")"):
                    ip = part[1:-1]
            at_index = parts.index("at")
            if at_index + 1 < len(parts):
                mac = parts[at_index + 1]
            devices.append({"ip": ip, "mac": mac})

    return devices


# ============================================================
#  SECTION C: File I/O — Text Files
# ============================================================
#
#  *** TASK 1 *** Complete these two functions:
#
#  Hints:
#    - write_to_log: open file in APPEND mode ("a")
#      and write the entry followed by "\n"
#    - read_log: open file in READ mode ("r")
#      and return file.read()
#    - Use "with open(...) as file:" for both
#
# ============================================================

def write_to_log(filename, entry):
    """Append a log entry to a text file."""
    # *** YOUR CODE HERE ***
    # Open the file in append mode ("a") using a with statement
    with open(filename, "a") as file:
        # Write the entry + "\n" to the file
        file.write(entry + "\n")


def read_log(filename):
    """Read and return the entire contents of a log file."""
    # *** YOUR CODE HERE ***
    # Open the file in read mode ("r") using a with statement
    with open(filename, "r") as file:
        # Return the result of file.read()
        return file.read()


# This function is COMPLETE — it uses write_to_log() above
def log_command_result(command_name, target, output, filename):
    """Log a command result to a text file with timestamp and separator."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = "[" + timestamp + "] " + command_name + " " + target + "\n"
    entry = entry + output
    entry = entry + "-" * 40
    write_to_log(filename, entry)


# ============================================================
#  SECTION D: File I/O — CSV Files
# ============================================================
#
#  *** TASK 2 *** Complete these two functions:
#
#  Hints:
#    - log_to_csv: open file in append mode with newline=""
    """Log a command result to a csv file."""
#      create csv.writer(file), then call writer.writerow([...])
#    - read_csv_log: open file in read mode with newline=""
#      create csv.reader(file), loop through rows,
#      print each row joined by " | "
#
# ============================================================

LOG_FILE = "diagnostics.csv"

def log_to_csv(filename, command, target, result, status):
    """Append one row to the CSV log file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # *** YOUR CODE HERE ***
    # Open filename in append mode ("a") with newline=""
    with open(filename, "a", newline="") as file:
    # Create a csv.writer(file)
        writer = csv.writer(file)
    # Write one row: [timestamp, command, target, result, status]
        writer.writerow([timestamp, command, target, result, status])


def read_csv_log(filename):
    """Read and display all rows from the CSV log file."""
    # *** YOUR CODE HERE ***
    # Open filename in read mode ("r") with newline=""
    with open(filename, "r", newline="") as file:
    # Create a csv.reader(file)
        reader = csv.reader(file)
    # Loop through rows and print: " | ".join(row)
        for row in reader:
            print(" | ".join(row))


# This function is COMPLETE — it uses the CSV functions above
def analyze_csv_log(filename):
    """Read the CSV log and print a summary analysis."""
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) == 0:
        print("Log is empty.")
        return

    total = len(rows)
    print("Total entries: " + str(total))

    command_counts = {}
    status_counts = {}

    for row in rows:
        command = row[1]
        status = row[4]

        if command in command_counts:
            command_counts[command] = command_counts[command] + 1
        else:
            command_counts[command] = 1

        if status in status_counts:
            status_counts[status] = status_counts[status] + 1
        else:
            status_counts[status] = 1

    print("\nCommands run:")
    for cmd in command_counts:
        print("  " + cmd + ": " + str(command_counts[cmd]) + " time(s)")

    print("\nResults:")
    for status in status_counts:
        print("  " + status + ": " + str(status_counts[status]))


# ============================================================
#  SECTION E: Exception Handling
# ============================================================
#
#  *** TASK 3 *** Complete safe_read_log():
#
#  Hints:
#    - try: open and read the file
#    - except FileNotFoundError: print a friendly message
#    - finally: print "Log read attempt completed."
#    - Return the content on success, empty string "" on failure
#
# ============================================================

# These two functions are COMPLETE — provided for you
def safe_ping(host):
    """Run ping with error handling for timeouts and failures."""
    try:
        result = subprocess.run(
            ["ping", "-c", "3", host],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return "Ping failed: Host unreachable or request timed out."
    except subprocess.TimeoutExpired:
        return "Ping failed: Command timed out after 10 seconds."
    except Exception as e:
        return "Ping failed: " + str(e)


def safe_nslookup(domain):
    """Run nslookup with error handling."""
    try:
        result = subprocess.run(
            ["nslookup", domain],
            capture_output=True, text=True, timeout=10
        )
        return parse_nslookup(result.stdout)
    except subprocess.TimeoutExpired:
        return {"ip": "Error: Timed out", "status": "Failed"}
    except Exception as e:
        return {"ip": "Error: " + str(e), "status": "Failed"}


def safe_read_log(filename):
    """Read a log file with error handling for missing files."""
    # *** YOUR CODE HERE ***
    try:
    #     open the file in read mode
        with open(filename, "r", newline="") as file:
    #     read the content
    #     if content is empty: print "Log file is empty." and return ""
            content = file.read()
            if content == 0:
                print("Log file is empty")
                return ""
    #     else: return the content
            else:
                return file.read()
    except FileNotFoundError:
    #     print "No log file found. Run a diagnostic first."
        print("No log file found. Ru a diagnostic first")
    #     return ""
        return ""
    finally:
    #     print "Log read attempt completed."
        print("Log read attempt completed")
    pass


def get_valid_input(prompt, valid_options):
    """Keep asking for input until the user enters a valid option."""
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        else:
            print("Invalid input. Please enter one of: " + ", ".join(valid_options))


# ============================================================
#  SECTION F: The Integrated Program (COMPLETE — provided)
# ============================================================
# This section uses ALL the functions above.
# Once you complete Tasks 1-3, the full program will work.
# ============================================================

def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 34)
    print("   NETWORK DIAGNOSTIC LOGGER")
    print("=" * 34)
    print("1. Ping a host")
    print("2. DNS Lookup (nslookup)")
    print("3. Show Network Info (MAC/IP)")
    print("4. Show ARP Table (local devices)")
    print("5. View full log")
    print("6. Analyze log (summary)")
    print("7. Quit")
    print("=" * 34)


def do_ping():
    """Run a ping diagnostic and log the result."""
    host = input("Enter hostname to ping: ")
    print("Running ping on " + host + "...")

    output = safe_ping(host)
    ping_data = parse_ping(output)

    print("  Status:      " + ping_data["status"])
    print("  Packets:     " + str(ping_data["transmitted"]) + " sent, " + str(ping_data["received"]) + " received")
    print("  Packet Loss: " + ping_data["loss"])
    print("  Avg Latency: " + str(ping_data["avg_ms"]) + " ms")

    log_to_csv(LOG_FILE, "ping", host, ping_data["avg_ms"], ping_data["status"])
    log_command_result("PING", host, output, "network_log.txt")
    print("Result logged.")


def do_nslookup():
    """Run a DNS lookup and log the result."""
    domain = input("Enter domain to lookup: ")
    print("Running nslookup on " + domain + "...")

    dns_data = safe_nslookup(domain)

    print("  Status:  " + dns_data["status"])
    print("  Domain:  " + domain)
    print("  IP:      " + dns_data["ip"])

    log_to_csv(LOG_FILE, "nslookup", domain, dns_data["ip"], dns_data["status"])
    print("Result logged.")


def do_network_info():
    """Get and display network interface info, log to CSV."""
    print("Fetching network info...")
    hostname = get_hostname()

    try:
        output = get_network_info()
        net_data = parse_mac_address(output)

        print("  Hostname:    " + hostname)
        print("  MAC Address: " + net_data["mac"])
        print("  IP Address:  " + net_data["ip"])

        log_to_csv(LOG_FILE, "ifconfig", "en0", net_data["mac"] + " / " + net_data["ip"], "Captured")
        print("Result logged.")
    except Exception as e:
        print("  Error: " + str(e))
        log_to_csv(LOG_FILE, "ifconfig", "en0", "Error", "Failed")


def do_arp_table():
    """Show all devices on the local network."""
    print("Scanning local network (ARP table)...")

    try:
        output = get_arp_table()
        devices = parse_arp_table(output)

        if len(devices) == 0:
            print("  No devices found.")
        else:
            print("  Found " + str(len(devices)) + " device(s):\n")
            for device in devices:
                print("    IP: " + device["ip"] + "  |  MAC: " + device["mac"])

        log_to_csv(LOG_FILE, "arp", "local", str(len(devices)) + " devices", "Captured")
        print("\nResult logged.")
    except Exception as e:
        print("  Error: " + str(e))


def do_view_log():
    """Display the full CSV log."""
    print("\n=== FULL LOG ===")
    try:
        with open(LOG_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) == 0:
                print("Log is empty.")
            else:
                for row in rows:
                    print(" | ".join(row))
    except FileNotFoundError:
        print("No log file found. Run a diagnostic first.")


def do_analyze():
    """Read the CSV log and show a summary analysis."""
    print("\n=== LOG ANALYSIS ===")
    try:
        analyze_csv_log(LOG_FILE)
    except FileNotFoundError:
        print("No log file found. Run some diagnostics first.")


def main():
    """Main program loop — the full Network Diagnostic Logger."""
    hostname = get_hostname()
    print("Welcome to the Network Diagnostic Logger!")
    print("Running on: " + hostname)

    while True:
        display_menu()
        choice = get_valid_input(
            "Enter your choice (1-7): ",
            ["1", "2", "3", "4", "5", "6", "7"]
        )

        if choice == "1":
            do_ping()
        elif choice == "2":
            do_nslookup()
        elif choice == "3":
            do_network_info()
        elif choice == "4":
            do_arp_table()
        elif choice == "5":
            do_view_log()
        elif choice == "6":
            do_analyze()
        elif choice == "7":
            print("Goodbye! Your log is saved in " + LOG_FILE)
            break


# ============================================================
#  TEST YOUR WORK
# ============================================================
# After completing Tasks 1-3, uncomment the line below to run:
main()
# ============================================================