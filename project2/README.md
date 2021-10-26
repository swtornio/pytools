# Project 2 - Web Header Reporting

Scenario: Red Planet has assigned you to do a web app penetration test against a few target domains. There are a few findings that your team regularly report on, but aren't very fun to detect or write up. As such, you are looking to automate this portion of your test so that you can spend more time going for something more critical. 

## Beginner Task: Write a script that will have the user input a HTTPS URL. The script should pull down the web headers for the URL entered and report back if the Strict-Transport-Security header is missing. 

## Intermediate Task: Have the script run multiple URLs from a file and process them all at once. Additionally, have it output both the URL and the IP address of each URL missing the Strict-Transport-Security header.

## Expert: Have the code perform all of the tasks above while also checking for the Content-Security-Policy and X-Frame-Options header, also reporting back if they are missing. It should also detect if a Server header is present, if it is it should return the value of the header.

## Bonus: Have the script evaluate if the URL is HTTP or HTTPS. If it is HTTP, it should ignore the need for a Strict-Transport-Security header while still evaluating all the others.


URLs to start with:
https://www.redsiege.com/
https://www.yahoo.com/
https://www.usbank.com/index.html
https://www.sidretail.com/
https://www.microsoft.com/en-us