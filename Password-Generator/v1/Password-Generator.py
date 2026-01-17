#!/usr/bin/env python3
import random
import os 
from pathlib import Path 
BASE_DIR = Path(__file__).resolve().parent
class Password:
        def __init__(self,length,numberOfNumbers,numberOfSymbols,numberOfLowercase,numberOfUppercase):
            self.length = length
            self.numberOfNumbers = numberOfNumbers
            self.numberOfSymbols = numberOfSymbols
            self.numberOfLowercase = numberOfLowercase
            self.numberOfUppercase = numberOfUppercase
def main():
    print("Welcome to the password generator")
    while True:
        os.system("clear")
        print("Choose your option:")
        print("1 - Generate a password")
        print("2 - View saved passwords")
        print("99 - Quit")
        choice = input()
        if choice == "1":
            parameters = GetParameters()
            password = GeneratePassword(parameters)
            OutputPassword(password)
        elif choice == "2":
            viewFile()
        elif choice == "99":
            break
def GetParameters():
    while True:
        os.system("clear")
        print("Enter how many of each option you want")
        length = int(input("Length:"))
        numberOfNumbers = int(input("Numbers"))
        numberOfSymbols = int(input("Symbols"))
        numberOfLowercase = int(input("Lowercase characters"))
        numberOfUppercase = int(input("Uppercase characters"))
        if (numberOfNumbers != int) or \
        (numberOfSymbols != int) or \
        (numberOfLowercase != int) or \
        (numberOfUppercase != int):
            print("You didn't enter a number, try again")
        if numberOfNumbers + numberOfSymbols + numberOfLowercase + numberOfUppercase != length:
            print("What you selected does not match the length")
            choice = input("Do you want to adjust the length?(Y/N)")
            if (choice == "Y") or \
                (choice == "y"):
                length = numberOfNumbers + numberOfSymbols + numberOfLowercase + numberOfUppercase
                break
            elif (choice == "N") or \
                (choice == "n"):
                continue
            else:
                print("Thats not an option, try again")
        else:
            break
    parameters = Password(
    length=length, 
    numberOfNumbers = numberOfNumbers,
    numberOfSymbols = numberOfSymbols,
    numberOfLowercase = numberOfLowercase,
    numberOfUppercase = numberOfUppercase 
)
    return parameters 
def GeneratePassword(parameters):
    passwordCharacters = []
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = r"""~`!@#$%^&*()_-+={[}]|\:;"'<,>./?"""
    numbers = "1234567890"
    for x in range(parameters.numberOfNumbers):
        passwordCharacters.append(random.choice(numbers))
    for x in range(parameters.numberOfSymbols):
        passwordCharacters.append(random.choice(symbols))
    for x in range(parameters.numberOfLowercase):
        passwordCharacters.append(random.choice(lowercase))
    for x in range(parameters.numberOfUppercase):
        passwordCharacters.append(random.choice(uppercase))
    random.shuffle(passwordCharacters)  
    password = ''.join(passwordCharacters)

    return password
def OutputPassword(password):
    os.system("clear")
    print("Your password is",password)
    choice = input("Would you like to save this password to a file?(Y/N)")
    if (choice == "Y") or \
    (choice == "y"):
        with open(BASE_DIR / "passwords.txt","a")as myfile:
            Pass = myfile
            Pass.write(password+"\n")     
def viewFile():
    with open(BASE_DIR / "passwords.txt","r")as myfile:
        passwords = myfile.read()
    print(passwords)
    print("Press ENTER to exit")
    input()
main()
