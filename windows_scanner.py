import os
import sys
import subprocess
import ctypes
import argparse
print("Welcome to the Web Scanner for Windows")
print("This script is designed to run on Windows. If u have a Linux system, please use the other script (scanner.py).")
def check_update():
    """Check if the script is up to date."""
    try:
        # Check for updates using git
        subprocess.run(["git", "pull"], check=True)
        print("Script is up to date.")
    except subprocess.CalledProcessError:
        print("Failed to check for updates. Please update manually.")
        sys.exit(1)
    except FileNotFoundError:
        print("Git is not installed. Please install git to check for updates.")
        sys.exit(1)
def check_administrator():
    """Check if the script is running with administrator privileges."""
    if os.name == 'nt':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("This script requires administrator privileges.")
            print("Please run the script as an administrator.")
            sys.exit(1)
check_administrator()
def run_nikto(target):
    """Run Nikto against the target."""
    print(f"Running Nikto against {target}...")
    subprocess.run(["nikto", "-h", target])
def run_whatweb(target):
    """Run WhatWeb against the target."""
    print(f"Running WhatWeb against {target}...")
    subprocess.run(["whatweb", target])
def run_nmap(target):
    """Run Nmap against the target."""
    print(f"Running Nmap against {target}...")
    subprocess.run(["nmap -vvv --min-rate 10000 -T4 -Pn -p- -oN escaneo.txt", target])
def full_scan(target):
    """Run a full scan against the target."""
    print(f"Running full scan against {target}...")
    subprocess.run(["nikto", "-h", target])
    subprocess.run(["whatweb", target])
    subprocess.run(["nmap -vvv --min-rate 10000 -T4 -Pn -p- -oN escaneo.txt", target])


def main():
    parser = argparse.ArgumentParser(description="Host Scanning Tool by russell")
    parser.add_argument("target", help="Target host (IP or domain)")
    parser.add_argument(
        "--mode", 
        choices=["full", "whatweb", "nmap", "nikto"],
        metavar="'full', 'whatweb', 'nmap', 'nikto'", 
        default="full", 
        help="Scan mode: full (default), whatweb, nmap, or nikto"
    )

    args = parser.parse_args()

    if args.mode == "full":
        full_scan(args.target)
    elif args.mode == "whatweb":
        run_whatweb(args.target)
    elif args.mode == "nmap":
        run_nmap(args.target)
    elif args.mode == "nikto":
        run_nikto(args.target)

def install_dependencies():
    """Install required dependencies."""
    print("Installing required dependencies...")
    subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"])
    subprocess.run(["choco", "install", "-y", "nikto"])
    subprocess.run(["choco", "install", "-y", "whatweb"])
    subprocess.run(["choco", "install", "-y", "nmap"])
    subprocess.run(["choco", "install", "-y", "git"])
    print("Dependencies installed successfully.")

    if not check_administrator():
        print("Please run the script as an administrator.")
        sys.exit(1)

print("Do you hsvr all the dependencies installed? (y/n)")
installar = input()
if installar.lower() == 'y' or installar.lower() == 'yes':
    print("All dependencies are installed.")
    main()
if installar.lower() == 'n' or installar.lower() == 'no':
    print("Installing dependencies...")
    install_dependencies()
    print("Dependencies installed successfully.")