#!/usr/bin/env python3
import shutil
import os
import sys

# function definitions

def is_yes(input):
    lower = input.lower()
    return lower == "y" or lower == "yes"


# field definitions

apps = ["git", "vim", "zsh"]


# configuration script

print("Before you begin, please ensure that you've installed the following applications:")
print(" ".join(apps) + "\n")
print("Do you wish to continue? (y/n)")
if !is_yes(input()):
    sys.exit(0)


for file in os.listdir("home"):
    location = os.path.join("home", file)
    home = os.path.expanduser("~")
    if os.path.isdir(location):
        print("moving dir '" + location + "' to '" + home + "'")
        shutil.copytree(location, home)
        shutil.rmtree(location)
    else:
        print("moving file '" + location + "' to '" + home + "'")
        shutil.move(location, home)

print("User setup complete. Would you like to configure global settings as well? (y/n)")
    if is_yes(input()):
        for file in os.listdir("root"):
            location = os.path.join("root", file)
            root = "/"
            if os.path.isdir(location):
                print("moving dir '" + location + "' to '" + home + "'")
                shutil.copytree(location, home)
                shutil.rmtree(location)
            else:
                print("moving file '" + location + "' to '" + home + "'")
                shutil.move(location, home)
print("Cleaning up...");
os.chdir("..")
shutil.rmtree("linux-config")
print("All done!")
    
else:
    print("You'll probably want to use one of these to install them, then:")
    print("sudo pacman -S " + " ".join(apps))
    print("sudo apt-get install " + " ".join(apps))
    print("sudo yum install " + " ".join(apps) + "\n")
