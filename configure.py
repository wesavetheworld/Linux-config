#!/usr/bin/env python3
import shutil
import subprocess

# function definitions

def is_yes(input):
    lower = input.lower()
    return lower == "y" or lower == "yes"


# field definitions

apps = ["vim", "zsh"]


# configuration script

print("Before you begin, please ensure that you've installed the following applications:")
print(" ".join(apps) + "\n")
print("Do you wish to continue? (y/n)")

if(is_yes(input())):
    # install code goes here
    
    for file in os.listdir("home"):
        shutil.copytree(os.path.join("home", file"), "~")
        
    # clean up the repo
    shutil.rmtree(".git")


else:
    print("You'll probably want to use one of these to install them, then:")
    print("sudo pacman -S " + " ".join(apps))
    print("sudo apt-get install " + " ".join(apps))
    print("sudo yum install " + " ".join(apps) + "\n")
