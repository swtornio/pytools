
# https://ipgeolocation.io/documentation/ip-geolocation-api.html

import requests
import argparse
import configparser
import ipaddress
import pandas
from ipwhois import IPWhois

# store the API key in an external file and make sure to add the file
# to .gitignore

cfg = configparser.ConfigParser()
cfg.read('ipgeo.cfg')

IPGEO_KEY = cfg.get('KEYS', 'api_key', raw='')
IPGEO_URL = "https://api.ipgeolocation.io/ipgeo"

provided_target = ""
results = list()


def locate_ipgeo(ip):
    '''Query IP Geo database for given IP and print Owner'''
    global results, provided_target
    try:
        resp = requests.get(f'{IPGEO_URL}?apiKey={IPGEO_KEY}&ip={ip}')
        location_info = resp.json()
        cidr_network = lookup_rdap(ip)
        results.append([ip, location_info["isp"], location_info["city"],
                        location_info["country_name"], provided_target,
                        cidr_network])
        print(f'{ip} from {provided_target} is owned by {location_info["isp"]}, '
              f'located in {location_info["city"]}, {location_info["country_name"]}.')
    except:
        pass


def lookup_rdap(ip):
    addr = IPWhois(ip)
    try:
        addr_data = addr.lookup_rdap(depth=1)
        return addr_data['network']['cidr']
    except:
        return 'CIDR lookup failed'


def main():

    global provided_target

    parser = argparse.ArgumentParser(
        description='Search for a provided list of queries.')
    parser.add_argument('-i', '--ip', default=False,
                        help='Look up a single IP')
    parser.add_argument('-c', '--cidr', default=False,
                        help='Look up a CIDR range')
    parser.add_argument('-f', '--file', default=False,
                        help='Load IPs and/or CIDR ranges from file')
    parser.add_argument('-o', '--output', default=False,
                        help='Log CSV results to this file')
    args = parser.parse_args()

    if args.ip:
        provided_target = args.ip
        locate_ipgeo(args.ip)
    if args.cidr:
        provided_target = args.cidr
        # get first address in range, perform lookup.
        addresses = list(ipaddress.ip_network(args.cidr).hosts())
        locate_ipgeo(addresses[0])
    if args.file:
        with open(args.file, "r") as f:
            targets = [line.strip() for line in f.readlines()]
            for target in targets:
                # check if it's an IP or a CIDR
                provided_target = target
                if "/" in target:
                    addresses = list(ipaddress.ip_network(target).hosts())
                    locate_ipgeo(addresses[0])
                else:
                    locate_ipgeo(target)

    if args.output:
        df_file = pandas.DataFrame(results, columns=['ip', 'Owner', 'City', 'Country',
                                                     'Provided Target', 'CIDR Block'])
        df_file.to_csv(args.output)


if __name__ == '__main__':
    main()
