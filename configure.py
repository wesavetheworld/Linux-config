#!/usr/bin/env python3

def isYes(input):
    lower = input.lower()
    return lower == "y" || lower == "yes"

apps = ["vim", "zsh"]

print("Before you begin, please ensure that you've installed the following applications:")
print(" ".join(apps) + "\n")
print("Do you wish to continue? (y/n)")

if(isYes(raw_input())):
    # install code goes here
else:
    print("You'll probably want to use one of these to install them, then:")
    print("sudo pacman -S " + " ".join(apps))
    print("apt-get install " + " ".join(apps))
    print("yum install " + " ".join(apps) + "\n")
