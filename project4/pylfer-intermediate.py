# Project 4 - Pilfer for Passwords!

# Scenario: While working with your teammates at Red Planet on an internal 
# penetration test, you found lots of files spread across open SMB shares. 
# Using another tool you have downloaded these files to your local machine. 
# Now you need to find out if these files contain any sensitive data!

## Intermediate Task: Add functionality to the script that will enable it 
# to search the contents of files for strings containing sensitive information 
# like "password" "username", "apikey", etc.

import argparse
import os

parser = argparse.ArgumentParser(
    description='Search files for a provided list of filenames.')
parser.add_argument('--dir', default='.',
                    help='Directory containing files to search')
parser.add_argument('--filenames', help='File containing filenames to search for')
parser.add_argument('--strings', help='File containing strings to search for within files')

args = parser.parse_args()

# starting path - make an arg
path = args.dir

if args.filenames:
    targets_file = args.filenames
    # populate from targets file
    with open(targets_file) as t:
        targets = t.read().splitlines()

    # traverse the path and identify target files
    for (root, dirs, file) in os.walk(path):
        for name in file:
            for target in targets:
                if target.lower() in name.lower():
                    print(os.path.join(root, name))

if args.strings:
    strings_file = args.strings
    with open(strings_file) as s:
        strings = s.read().splitlines()
    
    for (root, dirs, file) in os.walk(path):
        for name in file:
            try:
                with open(os.path.join(root, name)) as f:
                    for line in f:
                        for string in strings:
                            if string.lower() in line.lower():
                                print(f"{string} found in {os.path.join(root, name)}")
            except:
                pass


