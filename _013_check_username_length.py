# Program to check if username has less than 10 characters

username = input("Enter your username:\n")
if len(username)<10:
    print("Username has less than 10 characters")
else:
    print("Username has equal to or more than 10 characters")