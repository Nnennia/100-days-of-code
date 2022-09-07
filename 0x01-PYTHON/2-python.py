year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print("Leap year.")
elif year / 100:
        print("Not leap year.")
elif year % 4 == 0:
    print("Leap year.")
else:
        print("Not leap year.")

# or
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year.")
else:
    print("No leap year.")
