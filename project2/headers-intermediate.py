# Intermediate Task: Have the script run multiple URLs from a file and process them all 
# at once. Additionally, have it output both the URL and the IP address of each URL
# missing the Strict-Transport-Security header.

import argparse
import requests

def check_header(url):
	# have to keep the connection open to query the IP
	# could do a dns lookup, but if there are multiple IPs
	# you wouldn't actually know it was the host you connected to
	with requests.get(url, stream=True) as r:
		ip = r.raw._original_response.fp.raw._sock.getpeername()[0]
		sts_header = r.headers.get('Strict-Transport-Security')
		if sts_header != None:
			print(f"STS Header set as {sts_header} for {url} at {ip}.\n")
		else:
			print(f"STS Header not set for {url} at {ip}.\n")


def main():

	parser = argparse.ArgumentParser(description='Check headers for provided URLs.')
	parser.add_argument('--host', help='Check a single host')
	parser.add_argument('--input', help='File containing multiple URLs')

	args = parser.parse_args()
	if args.host:
		check_header(host)

	if args.input:
		with open(args.input, 'r') as f:
			for address in f.readlines():
				check_header(address.strip())



if __name__ == '__main__':
    main()