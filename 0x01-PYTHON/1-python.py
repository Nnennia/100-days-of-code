#check even or odd using module

number = int(input("Which number do ypu want to check? "))
result = number % 2

if result == 0:
    print("This is an even number .")
else:
    print("This is an odd number.")
