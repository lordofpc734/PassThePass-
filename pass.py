#search = input("website: ");__import__('clipboard').copy([i[1] for i in __import__('csv').reader(open('passwords.tsv','r')) if i[0] == search])
#search = input("website: ")
#print([i[2] for i in __import__('csv').reader(open('pass.csv','r')) if i[0] == search])
#print("password");print([i[1] for i in __import__('csv').reader(open('pass.csv','r')) if i[0] == search])
import csv
import subprocess
import clipboard
from time import sleep
import win32clipboard
search = input("Welcome to Pass The Pass!\n\nEnter website: ")
for i in csv.reader(open("pass.csv")):
  if i[0] == search:
    print("Username: {}".format(i[2]))
    clipboard.copy(i[2])
    input("Press [enter] to copy pass...")
    print("Password: {}".format(i[1]))
    clipboard.copy(i[1])
    input("Press [enter] to clear clipboard...")
    subprocess.call("clr_clipbrd.py", shell=True)
    exit(0)
print("{} not found".format(search))