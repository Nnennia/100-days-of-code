def login():
    global username
    global password
    flag = True
    while flag:
        username = input("Enter a username: ").lower()

        with open("pass/username.txt", "r+") as name:
            if username not in name.readline():
                name.write(username + "\n")

                password = input("Input a new password\n")
                if password != username:
                    flag = False
                    print("saved!\n")
                else:
                    print("Username cannot be password!")

            else:
                print("Username already exists")


def re_log():
    flag = True
    count = 0
    while flag:
        newpass = input("input password\n")
        if newpass != password:
            print("Wrong pasword!")
            count += 1
            if count == 5:
                flag = False
                print("TOO MANY GUESSES! ACCOUNT LOCKED")
        elif newpass == password:
            flag = False
            print(f"Login success!\nWelcome user: {username}!")


login()
re_log()
