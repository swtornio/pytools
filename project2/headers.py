#!/usr/bin/env python

import argparse
import requests
from concurrent.futures import ThreadPoolExecutor

# ANSI codes for some pretty terminal output

class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


# list of dictionaries containing server information
servers = list()


def check_header(url):
    # have to keep the connection open to query the IP
    # could do a dns lookup, but if there are multiple IPs
    # you wouldn't actually know it was the host you connected to
    global servers
    server_info = {"url": url,
                   "ip": "",
                   "tls": True,
                   "headers": {}}
    with requests.get(url, stream=True) as r:
        server_info['ip'] = r.raw._original_response.fp.raw._sock.getpeername()[
            0]
        # Create a dictionary to store headers in
        headers = {}
        if "https" in url:
            headers['Strict-Transport-Security'] = r.headers.get(
                'Strict-Transport-Security')
        else:
            server_info['tls'] = False
        headers['Content-Security-Policy'] = r.headers.get(
            'Content-Security-Policy')
        headers['X-Frame-Options'] = r.headers.get('X-Frame-Options')
        headers['Server'] = r.headers.get('Server')
        # Add the current server's headers to server_info, then
        # add the server to the global list of servers
        server_info['headers'] = headers
        servers.append(server_info)


def main():

    parser = argparse.ArgumentParser(
        description='Check headers for provided URLs.')
    parser.add_argument('--host', help='Check a single host')
    parser.add_argument('--input', help='File containing multiple URLs')

    args = parser.parse_args()
    if args.host:
        check_header(host)

    if args.input:
        url_list = []
        with open(args.input, 'r') as f:
            for address in f.readlines():
                url_list.append(address.strip())

        processes = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            for url in url_list:
                processes.append(executor.submit(check_header, url))

    for server in servers:
        print(f"{bcolors.OK}URL:{bcolors.RESET} {server['url']}\t"
        	  f"{bcolors.OK}IP:{bcolors.RESET} {server['ip']}")
        if server['tls'] == False:
            print(f"{bcolors.WARNING}Not an SSL/TLS connection, some "
            	  f"checks disabled.{bcolors.RESET}")
        for key, value in server['headers'].items():
            print(f'{bcolors.OK}{key}:{bcolors.RESET} {value}')
        print('\n')


if __name__ == '__main__':
    main()
