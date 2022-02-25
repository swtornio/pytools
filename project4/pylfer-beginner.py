# Project 4 - Pilfer for Passwords!

# Scenario: While working with your teammates at Red Planet on an internal 
# penetration test, you found lots of files spread across open SMB shares. 
# Using another tool you have downloaded these files to your local machine. 
# Now you need to find out if these files contain any sensitive data!

## Beginner Task: Write a script that will search file names for files that 
# could contain sensitive information. Names such as web.config, passwords.txt, 
# SiteList.xml, etc.

# 1 - xxx iterate through a list of files, collecting the names
# 2 - xxx recurse through directories
# 3 - xxx get list of target filenames from an input file
# 4 - xxx check list of (case-insensitive) filenames for target
# 5 - xxx output file (full path)

import argparse
import os

parser = argparse.ArgumentParser(
    description='Search files for a provided list of filenames.')
parser.add_argument('--dir', default='.',
                    help='Directory containing files to search')
parser.add_argument('--targets', default='targets.txt', help='File containing names to search for')

args = parser.parse_args()

# starting path - make an arg
path = args.dir
targets_file = args.targets

# populate from targets file
with open(targets_file) as t:
    targets = t.read().splitlines()

# traverse the path and identify target files
for (root, dirs, file) in os.walk(path):
    for f in file:
        for target in targets:
            if target.lower() in f.lower():
                print(f"{root}/{f}")
