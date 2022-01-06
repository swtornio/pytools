# Project 3 - Brute Force!

Scenario: You are working on an internal penetration test for Red Planet and have found a system that your point of contact labeled as "mission critical" has SSH enabled. Due to other findings on the network you know that the security administrator has weak passwords on lots of critical systems. Knowing this, you believe that you can password spray/brute force your way to victory.

## Beginner Task: Write a script that will perform a password spray against the SSH service using a single username and password list. It should output each time a username/password combination is failed, and stop on a successful log in.

## Intermediate Task: Give your script the added functionality to spray using a list of usernames and a single password, using lists for both usernames and passwords, as well as a traditional brute force options.

## Expert Task: Add the option to limit login attempts based on time. Example, run 5 login attempts, wait 60 seconds, run 5 more attempts, wait 60 seconds, repeat.

In order to test this you will need a service running SSH. I suggest setting up something on your local network to test against. Be mindful when setting this up, if you put something internet facing with a weak username/password combination you run the risk at someone on the internet doing the same thing we are and getting popped.


(env) mac@MacBook-Pro project3 % python ssh_login.py --help                                   
usage: ssh_login.py [-h] [-t TARGET] [-p PORT] [--credfile CREDFILE] [--brute] [--userfile USERFILE] [--spray]
                    [--password PASSWORD] [--stealth] [--attempts ATTEMPTS] [--delay DELAY]

Search for a provided list of queries.

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target hostname or IP
  -p PORT, --port PORT  SSH port
  --credfile CREDFILE   Load comma-separated credentials from file for brute force
  --brute               Brute force attack using comma-separated file of usernames and passwords
  --userfile USERFILE   Load usernames from file for password spray
  --spray               Perform password spray using provided file containing usernames and a specified password
  --password PASSWORD   Password to use with --spray
  --stealth             Perform a number of logins, then delay a specified time
  --attempts ATTEMPTS   Number of attempts before delay.
  --delay DELAY         Time to delay between attempts (in seconds)