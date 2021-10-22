# Project 1 - The Scope!

Scenario: Congrats, your Penetration testing company Red Planet has landed an external assessment for Microsoft! Your point of contact has give you a few IP addresses for you to test. Like with any test you should always verify the scope given to you to make sure there wasn't a mistake.

## Beginner Task: Write a script that will have the user input an IP address. The script should output the ownership and geolocation of the IP. The output should be presented in a way that is clean and organized in order to be added to your report.

## Intermediate Task:  Have the script read multiple IP addresses from a text file and process them all at once.

## Expert Task:Have the script read from a file containing both single IP addresses and CIDR notation, having it process it both types.

Here are your IP addresses to check:
```
131.253.12.5
131.91.4.55
192.224.113.15
199.60.28.111
```

For the Expert Task here are two networks in CIDR notation:
```
20.128.0.0/16
208.76.44.0/22
```

```
% python scoper.py -h                                    
usage: scoper.py [-h] [-i IP] [-c CIDR] [-f FILE] [-o OUTPUT]

Search for a provided list of queries.

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        Look up a single IP
  -c CIDR, --cidr CIDR  Look up a CIDR range
  -f FILE, --file FILE  Load IPs and/or CIDR ranges from file
  -o OUTPUT, --output OUTPUT
                        Log CSV results to this file
```