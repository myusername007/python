import re

password = input("Password: ")

def validate_password(pw):
    letter = re.search("[A-Z]", pw)
    number = re.search("[0-9]", pw)
    ss = re.search("[!@#$%^&*]", pw)
    if letter and number and ss:
        print("Your password is good!\n")
    else: print("Weak password!\n")

validate_password(password)