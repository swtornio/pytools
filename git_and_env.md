
# Create a GitHub repo and clone it

First, create a repository using the github web interface. If you pick a license, choose something open like MIT, Apache, BSD. If you pick GPL for a coding group where everyone is cribbing off each other, you're just introducing complications and infecting everyone's code with your choice.

If you haven't already done so, upload an SSH public key in Settings/SSH and GPG keys.

Configure your github user information locally (this is from memory, I'll update if someone corrects me)
`git config --global user.name "username"`
`git config --global user.email "me@here.com"`


## Clone the repo

In the repo, click the green Code button at the upper right and select the SSH clone tab, copy the address string and clone

```
steve@Stephens-MacBook-Pro src % git clone git@github.com:swtornio/pytools.git
Cloning into 'pytools'...
Enter passphrase for key '/Users/steve/.ssh/id_rsa': 
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (5/5), done
```

# Create a python environment for group projects

Create an environment for the class. Python environments are a handy way to keep dependencies from various projects from introducing conflicts.

```
steve@Stephens-MacBook-Pro pytools % python3 -m venv env
steve@Stephens-MacBook-Pro pytools % source env/bin/activate
(env) steve@Stephens-MacBook-Pro pytools % python --version
Python 3.8.2
```

