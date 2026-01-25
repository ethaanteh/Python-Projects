import random
from pathlib import Path 
BASE_DIR = Path(__file__).resolve().parent
class User:
    def __init__(self,username,password):
        self.username = username 
        self.password = password
def main():
    print("Welcome to the Password Generator")
    while True:
        print("Pick your option: ")
        print("1 - Generate a password")
        print("2 - Login and view passwords")
        print("99 - exit")
        #try:
        choice = int(input())
        if choice == 1:
            length, upper, lower, numbers, symbols, min_numbers, min_symbols = get_parameters()
            password = generate_password(length, upper, lower, numbers, symbols, min_numbers, min_symbols)
            output_password(password)
        elif choice == 2:
            login_menu()
        elif choice == 99:
            break 
        else:
            print("Thats not an option try again")
    #except ValueError:
            #print("Enter a valid digit, try again")
def get_parameters():
    while True:
        min_characters = 0
        print("Enter the parameters you want for each option")
        length = int(input("Length: "))
        #upper
        upper = input("Uppercase(y/n): ").lower()
        if(
            upper == "y"
        ):
            min_characters += 1
        elif(
            upper == "n"
        ):
            pass
        else:
            print("That's not an option, try again")
            continue
        #lower
        lower = input("Lowercase(y/n): ").lower()
        if (
            lower == "y"
        ):
            min_characters += 1
        elif(
            lower == "n"
        ):
            pass
        else:
            print("That's not an option, try again")
            continue
        #numbers
        numbers = input("Number(s)(y/n): ").lower()
        if (
            numbers == "y"
        ):
            min_numbers = input("Would you like to set a minimum amount of numbers?(y/n): ").lower()
            if (
                min_numbers == "y"
            ):
                max_numbers = length - min_characters 
                while True:
                    min_numbers = input(f"how many minimum numbers would you like to set?(1 - {max_numbers})")
                    try:
                        min_numbers = int(min_numbers)
                        if 1 <= min_numbers <= max_numbers:
                            break
                        else:
                            print(f"Enter a number between 1 and {max_numbers}")
                    except ValueError:
                        print("You must enter a number, try again")   
        elif( 
            numbers == "n"
        ):
            min_characters += 1
        else:
            print("That's not an option, try again")
            continue
        symbols = input("Special character(s)(y/n): ").lower()
        if( 
            symbols == "y"
        ):
            min_symbols = input("Would you like to set a minimum amount of special characters?(y/n): ").lower()
            if( 
                min_symbols == "y"
            ):
                max_symbols = length - min_characters - min_numbers
                while True:
                    min_symbols = input(f"how many minimum numbers would you like to set?(1 - {max_symbols})")
                    try:
                        min_symbols = int(min_symbols)
                        if 1 <= min_symbols <= max_symbols:
                            break
                        else:
                            print(f"Enter a number between 1 and {max_symbols}")
                    except ValueError:
                        print("You must enter a number, try again")
        elif(
            symbols == "n"
        ):
            min_characters +=1
        else:
            print("That's not an option, try again")
            continue
        return length, upper, lower, numbers, symbols, min_numbers, min_symbols
def generate_password(length, upper, lower, numbers, symbols, min_numbers, min_symbols):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    upper_and_lower = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    number = "1234567890"
    symbol = r"""~`!@#$%^&*()_-+={[}]|\:;"'<,>./?"""
    password_characters = []
    if(
        numbers == "y"
    ):
        for x in range(min_numbers):
            password_characters.append(random.choice(number))
    if(
        symbols == "y"
    ):
        for x in range(min_symbols):
            password_characters.append(random.choice(symbol))
    if(
        upper == "y" and lower == "y"
    ):
        password_characters.append(random.choice(uppercase))
        password_characters.append(random.choice(lowercase))
        for x in range((length - min_numbers)- min_symbols - 2):
            password_characters.append(random.choice(upper_and_lower))
    elif(
        upper == "y" and lower == "n"
    ):
        password_characters.append(random.choice(uppercase))
    elif( 
        upper == "n" and lower == "y"
    ):
        password_characters.append(random.choice(lowercase))
    random.shuffle(password_characters)
    password = ''.join(password_characters)
    return password
def output_password(password):
    print (f"Your password is {password}")
def login_menu():
    print("Enter your option")
    print("1 - Returning user")
    print("2 - New user")
    try:
        choice = int(input())
        if choice == 1:
            pass
            #user_login(user_info)
        elif choice == 2:
            new_user()
        else:
            print("That's not an option, try again")
    except ValueError:
        print("Enter a valid digit, try again")
def user_login():
    pass
def new_user():
    username = ""
    password = ""
    user = input("Enter your username: ")
    passwd = input("Enter your password: ")
    user_check(user)
    with open(BASE_DIR / "user_info.txt","a",encoding="utf-8") as f:
        f.write(f"\n{user},{passwd}")
    with open(BASE_DIR / f"{user}-passwords.txt","w",encoding="utf-8") as f:
        f.write
def user_check(user):
    pass
if __name__ == "__main__":
    main()
