import os
import platform
import subprocess
import sys
import time

def ping_ip(ip):
    # Define the ping command based on the OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Execute the ping command
    command = ["ping", param, "1", ip]
    try:
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            return "!"  # IP is live
        else:
            return "n"  # No response
    except Exception as e:
        return "n"

def main():
    try:
        ip_count = int(input("How many IP addresses would you like to ping? "))
        ip_list = []
        for _ in range(ip_count):
            ip = input("Enter IP address: ")
            ip_list.append(ip)

        results = {ip: "" for ip in ip_list}  # Store ping results for each IP address

        print("Starting pings... Press Ctrl+C to stop.")
        sys.stdout.flush()

        while True:
            for ip in ip_list:
                status = ping_ip(ip)
                results[ip] += status  # Append the result to the string for this IP

                # Clear the screen and print updated results
                sys.stdout.write("\033c")  # This clears the terminal screen
                for ip, result in results.items():
                    sys.stdout.write(f"{ip}: {result}\n")
                sys.stdout.flush()

            time.sleep(1)  # Sleep for a second before next ping round

    except KeyboardInterrupt:
        print("\n\nPing test interrupted.")

if __name__ == "__main__":
    main()