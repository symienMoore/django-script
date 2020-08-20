import sys
import os

newdirectory = raw_input("name the directory: ")
newproject   = raw_input("name your project: ")

os.mkdir("/Users/symi/programming/" + newdirectory)
os.chdir("/Users/symi/programming/" + newdirectory)
os.system('virtualenv -p python3 venv')
os.system("source venv/bin/activate")
os.system('django-admin startproject ' + newproject)
os.system("code .")