# email = "python@gmail.com"
# pass = "1234"

email = input("Enter your email ")
# if email does not contain "@" we will show incorrect wont take password
if "@" in email:
    password = input("Enter password ")

    if email == "python@gmail.com" and password == "1234":
        print("Welcome to your profile")
    elif email == "python@gmail.com" and password != "1234":
        print("Password Incorrect")
        password = input("Enter password again")
        if password == "1234":
            print("Finally correct")
        else:
            print("Still incorrect")
    else:
        print("Incorrect credentials.")

else:
    print("Email is incorrect, Try again!")