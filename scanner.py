import subprocess
import argparse
import os
import sys
import ctypes

def linux():
    check_root()
    check_dependencies()
    print("Thansk you for using this script. Enjoy the experience.")
    target = input("Enter the target IP or domain: ")
    mode = input("Enter the scan mode (full, whatweb, nmap, nikto): ")
    if mode == "full":
        full_scan(target)
    elif mode == "whatweb":
        run_whatweb(target)
    elif mode == "nmap":
        run_nmap(target)
    elif mode == "nikto":
        run_nikto(target)
def windows():
    print("This script is designed to run on Linux.")
    print("You can use the other script  (windows_scanner.py) for Windows.")
    print("Exiting...")
    sys.exit(1)
def mac():
    print("This script is designed to run on Linux.")
    print("We are working on a Mac version.")
    print("Exiting...")
    sys.exit(1)

print("What is your os?")
print("1. Linux")
print("2. Windows")
print("3. Mac")
print("4. Other")
input_os = input("Enter the number of your OS: ")
if input_os == "1":
    linux()  
elif input_os == "2":
    windows()
elif input_os == "3":
    mac()
else:
    print("We do not recognize this OS.")
    print("Please use the Linux version.")
    print("Exiting...")
    sys.exit(1)

def check_update():
    """check if the script is up to date."""
    try:
        # Check for updates using git
        subprocess.run(["git", "pull"], check=True)
        print("Script is up to date.")
    except subprocess.CalledProcessError:
        print("Failed to check for updates. Please update manually.")
        sys.exit(1)
check_update()



def check_root():
    """Check if the script is running with root privileges."""
    if os.geteuid() != 0:
        print("This script requires root privileges.")
        print("Please run the script with sudo.")
        sys.exit(1)
    if input_os == "1":
        check_root()
def check_dependencies():
    """Check if required tools are installed."""
    required_tools = ["nikto", "whatweb", "nmap"]
    missing_tools = []

    for tool in required_tools:
        if subprocess.call(["which", tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE) != 0:
            missing_tools.append(tool)

    if missing_tools:
        print(f"Missing tools: {', '.join(missing_tools)}")
        print("Please install them before running this script.")
        instalar = input("Do you want to install them? (y/n): ")
        if instalar.lower() == 'y' or instalar.lower() == 'yes':
            print("Installing missing tools...")
            for tool in missing_tools:
                print(f"Installing {tool}...")
                subprocess.run(["sudo", "apt-get", "install", "-y", tool])
        else:
            print("Exiting...")
        sys.exit(1)
          
def run_nikto(target):
    print(f"Running Nikto on {target}...")
    subprocess.run(["nikto", "-h", target])

def run_whatweb(target):
    print(f"Running WhatWeb on {target}...")
    subprocess.run(["whatweb", target])

def run_nmap(target):
    print(f"Running Nmap on {target}...")
    subprocess.run(["nmap -vvv --min-rate 10000 -T4 -Pn -p- -oN escaneo.txt", target])

def full_scan(target):
    print(f"Performing a full scan on {target}...")
    run_whatweb(target)
    run_nmap(target)
    run_nikto(target)

def main():
    parser = argparse.ArgumentParser(description="Host Scanning Tool by russell")
    parser.add_argument("target", help="Target host (IP or domain)")
    parser.add_argument(
        "--mode", 
        choices=["full", "whatweb", "nmap", "nikto"],
        metavar="MODE", 
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

if __name__ == "__main__":
    main()
# End of the script
#Developed by Russell