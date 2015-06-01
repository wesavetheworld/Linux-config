#!/usr/bin/env python3
import shutil


# function definitions

def is_yes(input):
    lower = input.lower()
    return lower == "y" || lower == "yes"
    
def move_recursive(source, destination):
    shutil.copytree(source, destination)
    shutil.rmtree(source)


# field definitions

apps = ["vim", "zsh"]


# configuration script

print("Before you begin, please ensure that you've installed the following applications:")
print(" ".join(apps) + "\n")
print("Do you wish to continue? (y/n)")

if(isYes(raw_input())):
    # install code goes here
    move_recursive("home/*", "~")
    
    # clean up the repo
    shutil.rmtree(".git")
    
    
else:
    print("You'll probably want to use one of these to install them, then:")
    print("sudo pacman -S " + " ".join(apps))
    print("apt-get install " + " ".join(apps))
    print("yum install " + " ".join(apps) + "\n")
