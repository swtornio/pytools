
# Create a GitHub repo and clone it

First, create a repository using the github web interface. If you pick a license, choose something open like MIT, Apache, BSD. If you pick GPL for a coding group where everyone is cribbing off each other, you're just introducing complications and infecting everyone's code with your choice. Choose a default .gitignore file for Python.

If you haven't already done so, upload an SSH public key in Settings/SSH and GPG keys.

Configure your github user information locally (this is from memory, I'll update if someone corrects me)
```
git config --global user.name "username"
git config --global user.email "me@here.com"
```


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

# Create files, commit, and push to github

```
(env) steve@Stephens-MacBook-Pro pytools % ls
LICENSE		README.md	env		git_and_env.md

(env) steve@Stephens-MacBook-Pro pytools % git add git_and_env.md
(env) steve@Stephens-MacBook-Pro pytools % git commit -m "first commit of setup notes" git_and_env.md
[main 4ba77a1] first commit of setup notes
 1 file changed, 38 insertions(+)
 create mode 100644 git_and_env.md

(env) steve@Stephens-MacBook-Pro pytools % git push
Enter passphrase for key '/Users/steve/.ssh/id_rsa': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.02 KiB | 1.02 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:swtornio/pytools.git
   875a419..4ba77a1  main -> main
```
