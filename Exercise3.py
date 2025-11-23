username = input("Please Enter username: ")

if len(username) > 12:
    print("Username should not be more than 12 character")
elif not username.find(" ") == -1:
    print("Username can't contain spaces")
else:
    print(f"Welcome back {username} ")
