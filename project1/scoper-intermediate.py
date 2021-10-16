# Project 1 - The Scope!

# Scenario: Congrats, your Penetration testing company Red Planet has
# landed an external assessment for Microsoft! Your point of contact has
# give you a few IP addresses for you to test. Like with any test you
# should always verify the scope given to you to make sure there wasn't
# a mistake.

# Intermediate Task: Have the script read multiple IP addresses from a text 
# file and process them all at once.

# Bulk lookup
#  $  curl -X POST 'https://api.ipgeolocation.io/ipgeo-bulk?apiKey=API_KEY'
#  -H 'Content-Type: application/json'
#  -d '{ "ips": ["1.1.1.1", "1.2.3.4"] }'

# https://ipgeolocation.io/documentation/ip-geolocation-api.html

import requests

# store the API key in an external file and make sure to add the file
# to .gitignore
from config import IPGEO_KEY

IPGEO_URL = "https://api.ipgeolocation.io/ipgeo"

def locate(ip):
    '''Query IP Geo database for given IP and print Owner'''
    resp = requests.get(f'{IPGEO_URL}?apiKey={IPGEO_KEY}&ip={ip}')
    location_info = resp.json()
    print(f'{ip} is owned by {location_info["isp"]}, located in '
          f'{location_info["city"]}, {location_info["state_prov"]}.')


if __name__ == '__main__':
    with open("ips.txt", "r") as f:
        targets = [line.strip() for line in f.readlines()]
        for target in targets:
            locate(target)