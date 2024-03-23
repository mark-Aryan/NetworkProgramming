import sys
from ip_file_validator import ip_file_valid
from ip_addr_validator import ip_addr_valid
from ip_reachability import ip_reach
from ssh_connect import ssh_connection
from thread import create_threads

# Saving the list of IP address in ip.txt to a variable
ipList = ip_file_valid()


# Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ipList)

except KeyboardInterrupt:
    print("X Program aborted by user. Exiting. . . .")
    sys.exit()


# Verifying the reachability of IP address in the list
try:
    ip_reach(ipList)

except KeyboardInterrupt:
    print("X Program aborted by user. Exiting. . . .")
    sys.exit()


# Calling threads creation function for one or more SSH connections
create_threads(ipList, ssh_connection)

# End of Program
