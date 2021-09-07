##########################
# Euro Million
##########################
import random
import sys

users = [(0, "admin", "admin")]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")


try:
    _, username, password = username_mapping[username_input]
except KeyError as e:
    print("Your username is incorrect!")
    sys.exit()


major_numbers = random.sample(range(1, 50), 5)
star_numbers = random.sample(range(1, 12), 2)


if username_input == username and password_input == password:
    print(f"Euro Million Numbers: {major_numbers} - Luck Starts: {star_numbers}")
    print("")
    print("Good Luck!!!")
else:
    print("Your password is incorrect!")
