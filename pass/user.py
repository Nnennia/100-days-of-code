def user_name():
    global username
    flag = True
    while flag:
        with open("pass/username.txt", "r+") as name:
            username = input("Enter a username: ")
            if username not in name.read():
                if len(username) == 8:
                    print("saved!")
                    flag = False
                else:
                    print("Username must be 8 characters long!")
            else:
                print("Username already exists")


def passwrd():
    global password
    flag = True
    while flag:
        password = input("Input a new password\n")
        if len(password) == 8:
            if password != username:
                flag = False
                print("saved\n")
            else:
                print("Username cannot be password!")
        else:
            print("Password must be 8 characters long!")


def saved():
    with open("pass/username.txt", "r+") as name:
        name.write(username + ' ' + password + "\n")


def re_log():
    flag = True
    count = 0
    while flag:
        newpass = input("input your password to login\n")
        if newpass != password:
            print("Wrong pasword!")
            count += 1
            if count == 5:
                flag = False
                print("TOO MANY GUESSES! ACCOUNT LOCKED")
        elif newpass == password:
            flag = False
            print(f"Login success!\nWelcome user: {username}!")


user_name()
passwrd()
saved()
re_log()
