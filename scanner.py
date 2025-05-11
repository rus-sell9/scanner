import subprocess
import argparse
import os
import sys

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
    subprocess.run(["nmap", target])

def full_scan(target):
    print(f"Performing a full scan on {target}...")
    run_whatweb(target)
    run_nmap(target)

def main():
    parser = argparse.ArgumentParser(description="Host Scanning Tool by russell")
    parser.add_argument("target", help="Target host (IP or domain)")
    parser.add_argument(
        "--mode", 
        choices=["full", "whatweb", "nmap"], 
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