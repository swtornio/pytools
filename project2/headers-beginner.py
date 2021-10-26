# Beginner Task: Write a script that will have the user input a HTTPS URL.
# The script should pull down the web headers for the URL entered and report
# back if the Strict-Transport-Security header is missing.

import argparse
import requests

def main():

	parser = argparse.ArgumentParser(description='Search for a provided list of queries.')
	parser.add_argument('--host', help='Check a single host')

	args = parser.parse_args()
	url = args.host
	resp = requests.get(url)
	if resp.headers.get('Strict-Transport-Security') != None:
		print(f"STS Header set as {resp.headers.get('Strict-Transport-Security')}\n")
	else:
		print("STS Header not set.\n")


if __name__ == '__main__':
    main()