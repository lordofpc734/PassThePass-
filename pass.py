#search = input("website: ");__import__('clipboard').copy([i[1] for i in __import__('csv').reader(open('passwords.tsv','r')) if i[0] == search])
#search = input("website: ")
#print([i[2] for i in __import__('csv').reader(open('pass.csv','r')) if i[0] == search])
#print("password");print([i[1] for i in __import__('csv').reader(open('pass.csv','r')) if i[0] == search])
import csv
import clipboard
from time import sleep
import win32clipboard
search = input("Welcome to Pass The Pass?!\n\nEnter website: ")
for i in csv.reader(open('pass.csv','r')):
    if i[0] == search:
        print("Username: " + i[2])
        clipboard.copy(i[2])
        break
else:
    print(f"\"{search}\" not found")
###
sleep(0.3)
for i in csv.reader(open('pass.csv','r')):
    if i[0] == search:
        print("Password: " + i[1])
        clipboard.copy(i[1])
        break
input("\n\nPress Enter to clear clipboard.")
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.CloseClipboard()