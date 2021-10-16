# Project 1 - The Scope!

# Scenario: Congrats, your Penetration testing company Red Planet has
# landed an external assessment for Microsoft! Your point of contact has
# give you a few IP addresses for you to test. Like with any test you
# should always verify the scope given to you to make sure there wasn't
# a mistake.

# Intermediate Task: Have the script read multiple IP addresses from a text file and process them all at once.

# Bulk lookup
#  $  curl -X POST 'https://api.ipgeolocation.io/ipgeo-bulk?apiKey=API_KEY'
#  -H 'Content-Type: application/json'
#  -d '{ "ips": ["1.1.1.1", "1.2.3.4"] }'