# Project 1 - The Scope!

# Scenario: Congrats, your Penetration testing company Red Planet has
# landed an external assessment for Microsoft! Your point of contact has
# give you a few IP addresses for you to test. Like with any test you
# should always verify the scope given to you to make sure there wasn't
# a mistake.

# Expert Task:Have the script read from a file containing both single
# IP addresses and CIDR notation, having it process it both types.

# https://ipgeolocation.io/documentation/ip-geolocation-api.html

# TODO:
#   - use Rdap for lookups
#   - option to specify rdap or ipgeo

import requests
import argparse
import configparser
import ipaddress
import pandas

# store the API key in an external file and make sure to add the file
# to .gitignore

cfg = configparser.ConfigParser()
cfg.read('ipgeo.cfg')

IPGEO_KEY = cfg.get('KEYS', 'api_key', raw='')
IPGEO_URL = "https://api.ipgeolocation.io/ipgeo"

results = list()

def locate_ipgeo(ip):
    '''Query IP Geo database for given IP and print Owner'''
    global results
    resp = requests.get(f'{IPGEO_URL}?apiKey={IPGEO_KEY}&ip={ip}')
    location_info = resp.json()
    results.append([ip, location_info["isp"], location_info["city"],
                    location_info["country_name"]])
    print(f'{ip} is owned by {location_info["isp"]}, located in '
          f'{location_info["city"]}, {location_info["country_name"]}.')


def main():

    parser = argparse.ArgumentParser(
        description='Search for a provided list of queries.')
    parser.add_argument('-i', '--ip', default=False, help='Look up a single IP')
    parser.add_argument('-c', '--cidr', default=False, help='Look up a CIDR range')
    parser.add_argument('-f', '--file', default=False, help='Load IPs and/or CIDR ranges from file')
    parser.add_argument('-o', '--output', default=False, help='Log CSV results to this file')
    args = parser.parse_args()

    if args.ip:
        locate_ipgeo(args.ip)
    if args.cidr:
        # get first address in range perform lookup. 
        # TODO: check returned CIDR in rdap for match
        addresses = list(ipaddress.ip_network(args.cidr).hosts())
        locate_ipgeo(addresses[0])
    if args.file:
        with open(args.file, "r") as f:
            targets = [line.strip() for line in f.readlines()]
            for target in targets:
                # check if it's an IP or a CIDR
                if "/" in target:
                    addresses = list(ipaddress.ip_network(target).hosts())
                    locate_ipgeo(addresses[0])
                    locate_ipgeo(addresses[-1])
                else:
                   locate_ipgeo(target)

    if args.output:
        df = pandas.DataFrame(results, columns =['ip', 'Owner', 'City', 'Country'])
        df.to_csv(args.output)


if __name__ == '__main__':
    main()