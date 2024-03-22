import os
import sys


def ip_file_valid():
    # Firstly choose IP file by providing path of the file
    ip_file = str(input("Enter Path of your IP File (e.g. D:/user/IP_file.txt): "))

    if os.path.isfile(ip_file):
        print("IP File is Valid: \n ")

    else:
        print(f"File {ip_file} does not exist : (Please Check and try again.")
        sys.exit()

    # Open user selected file for reading (IP address file)
    selected_ip_file = open(ip_file, 'r')

    # Starting from the beginning of the file
    selected_ip_file.seek(0)

    # Reading each line (IP Address) from the file
    ip_list = selected_ip_file.readlines()

    # Closing File
    selected_ip_file.close()

    return ip_list

