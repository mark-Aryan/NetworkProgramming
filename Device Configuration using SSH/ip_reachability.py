import sys
import subprocess


# Checking IP Reachability
def ip_reach(ip_list):
    for ip in ip_list:
        ip = ip.rstrip("\n")

        ping_reply = subprocess.call('ping %s -n 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if ping_reply:
            print(f"{ip} is reachable: ")
            continue
        else:
            print(f"XX IP {ip} not reachable, check connectivity and try again.")
            sys.exit()

