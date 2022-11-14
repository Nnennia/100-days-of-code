import pandas


def login():
    flag = True
    count = 0
    while flag:
        username = input("Enter a username: ").lower()
        password = input("Input a new password: ")

        login = ({"username": [username], "password": [password]})
        data = pandas.DataFrame(login)
        data.to_csv("26-day/newpassword.csv")
        print("Re-enter new password to login")

        newpass = input("input password ")
        if newpass != password:
            print("Wrong password!")
            count += 1
            if count == 5:
                flag = False
                print("Too many guesses! Account locked")
            elif newpass == password:
                flag = False
                print(f"Login sucess!\nWelcome user: {username}!")


login()
