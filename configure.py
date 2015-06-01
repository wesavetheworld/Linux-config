#!/usr/bin/env python3
import shutil
import os

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

if is_yes(input()):
    for file in os.listdir("home"):
        location = os.path.join("home", file)
        if os.path.isdir(location):
            print("moving dir '" + location + "' to ~")
            shutil.copytree(location, "~")
            shutil.rmtree(location)
        else:
            print("moving file '" + location + "' to ~")
            shutil.move(location, "~")
    # clean up the repo
    # shutil.rmtree("../linux-config")
    print("All done!")
    
else:
    print("You'll probably want to use one of these to install them, then:")
    print("sudo pacman -S " + " ".join(apps))
    print("sudo apt-get install " + " ".join(apps))
    print("sudo yum install " + " ".join(apps) + "\n")
