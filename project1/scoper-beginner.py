# Project 1 - The Scope!

# Scenario: Congrats, your Penetration testing company Red Planet has
# landed an external assessment for Microsoft! Your point of contact has
# give you a few IP addresses for you to test. Like with any test you
# should always verify the scope given to you to make sure there wasn't
# a mistake.

## Beginner Task: Write a script that will have the user input an IP
## address. The script should output the ownership and geolocation of the
## IP. The output should be presented in a way that is clean and organized
## in order to be added to your report.

# Resources:
# https://ipgeolocation.io/

# Get geolocation for an IPv4 IP Address = 8.8.8.8
# $ curl 'https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=8.8.8.8'

# https://ipgeolocation.io/documentation/ip-geolocation-api.html

import requests
import configparser

# store the API key in an external file and make sure to add the file
# to .gitignore

cfg = configparser.ConfigParser()
cfg.read('ipgeo.cfg')

IPGEO_KEY = cfg.get('KEYS', 'api_key', raw='')
IPGEO_URL = "https://api.ipgeolocation.io/ipgeo"

def locate(ip):
    '''Query IP Geo database for given IP and print Owner'''
    resp = requests.get(f'{IPGEO_URL}?apiKey={IPGEO_KEY}&ip={ip}')
    location_info = resp.json()
    print(f'{ip} is owned by {location_info["isp"]}, located in '
          f'{location_info["city"]}, {location_info["state_prov"]}.')


if __name__ == '__main__':
    target_ip = input("Enter an IP to look up: ")
    locate(target_ip)
