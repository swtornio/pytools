# Expert: Have the code perform all of the tasks above while also checking for
# the Content-Security-Policy and X-Frame-Options header, also reporting back
# if they are missing. It should also detect if a Server header is present, if
# it is it should return the value of the header.

# Bonus: Have the script evaluate if the URL is HTTP or HTTPS. If it is HTTP,
# it should ignore the need for a Strict-Transport-Security header while still
# evaluating all the others.

import argparse
import requests
from concurrent.futures import ThreadPoolExecutor

# list of dictionaries
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
        headers = {}
        if "https" in url:
            headers['sts'] = r.headers.get('Strict-Transport-Security')
        else:
            server_info['tls'] = False
        headers['csp'] = r.headers.get('Content-Security-Policy')
        headers['xfo'] = r.headers.get('X-Frame-Options')
        headers['banner'] = r.headers.get('Server')
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
        print(f"URL: {server['url']}\tIP:{server['ip']}")
        print("Headers:")
        for key, value in server['headers'].items():
            print(key, value)
        print('\n')


if __name__ == '__main__':
    main()
