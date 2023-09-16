# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 14:48:41 2023

@author: Us
"""
import random
import string


characters = list(string.ascii_letters +string.digits +"!@#$^&%*()")

def generate_password():
    password_length = int(input("length of password u need to have ? "))
    
    random.shuffle(characters)
    
    password = []
    for i in range (password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = "".join(password)
    print(password)
option = input("Do you want to generate a password Yes or No ? ")
if option =="Yes" or option == "yes":
    generate_password()
elif option == "No" or option =="no":
    print("End ")   
else:
    print("invalid option")
    
