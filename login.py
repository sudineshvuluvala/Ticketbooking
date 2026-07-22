def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "admin" and password == "1234":
        print("Login Successful\n")
        return True
    else:
        print("Invalid Login")
        return False