#search = input("website: ");__import__('clipboard').copy([i[1] for i in __import__('csv').reader(open('passwords.tsv','r')) if i[0] == search])
#search = input("website: ")
#print([i[2] for i in __import__('csv').reader(open('pass.csv','r')) if i[0] == search])
#print("password");print([i[1] for i in __import__('csv').reader(open('pass.csv','r')) if i[0] == search])
import csv
import subprocess
import clipboard
from time import sleep
import win32clipboard
from fileinput import filename
from cryptography.fernet import Fernet
import os
extns = ".safe"
filename_1 = "passcopy.csv"
filename_2 = filename_1 + extns


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
#write_key()
#key = load_key()
#print("Decrypting CSV Database...")
#decrypt(filename_2, key)
#os.rename(filename_2, filename_1)
search = input("Welcome to Pass The Pass!\n\nEnter website: ")
for i in csv.reader(open("passcopy.csv")):
  if i[0] == search:
    print("Username: {}".format(i[2]))
    clipboard.copy(i[2])
    input("Press [enter] to copy pass...")
    print("Password: {}".format(i[1]))
    clipboard.copy(i[1])
    input("Press [enter] to clear clipboard & encrypt CSV db...")
    key = load_key()
    encrypt(filename_1, key)
    #subprocess.call("clr_clipbrd.py", shell=True)
    exit(0)
print("{} not found".format(search))
input("Press [enter] to clear clipboard & encrypt CSV db...")
key = load_key()
encrypt(filename_1, key)
#os.rename(filename_1, filename_2)
