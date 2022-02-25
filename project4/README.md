# Project 4 - Pilfer for Passwords!

Scenario: While working with your teammates at Red Planet on an internal penetration test, you found lots of files spread across open SMB shares. Using another tool you have downloaded these files to your local machine. Now you need to find out if these files contain any sensitive data!

## Beginner Task: Write a script that will search file names for files that could contain sensitive information. Names such as web.config, passwords.txt, SiteList.xml, etc.

## Intermediate Task: Add functionality to the script that will enable it to search the contents of files for strings containing sensitive information like "password" "username", "apikey", etc.

## Expert Task: Allow the user to specify the combinations of file names, types, and strings to search for. 

Bonus Task: Add recursive search.

```

$ python3 ./pylfer.py --help
usage: pylfer.py [-h] [--dir DIR] [--filenames FILENAMES] [--strings STRINGS]
                 [--extension EXTENSION]

Search files for a provided list of filenames.

optional arguments:
  -h, --help            show this help message and exit
  --dir DIR             Directory containing files to search
  --filenames FILENAMES
                        File containing filenames to search for
  --strings STRINGS     File containing strings to search for within files
  --extension EXTENSION
                        Search for strings in files with a specific extension


$ python3 ./pylfer.py --dir /home/danny/src/pytools/ --strings strings.txt --extension txt
password found in /home/danny/src/pytools/project3/default_creds.txt
password found in /home/danny/src/pytools/project4/strings.txt
username found in /home/danny/src/pytools/project4/strings.txt
apikey found in /home/danny/src/pytools/project4/strings.txt
password found in /home/danny/src/pytools/project4/targets.txt
```