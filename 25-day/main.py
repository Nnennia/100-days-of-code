# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [n * n for n in numbers]
# [n ** 2 for n in numbers]

# Write your code 👆 above:

# print(squared_numbers)

result = [n for n in numbers if n % 2 == 0]

# print(result)


def readsfile():
    with open("25-day/file1.txt") as f1, open("25-day/file2.txt") as f2:
        file1 = f1.readlines()
        file2 = f2.readlines()
        file1 = [int(n.strip()) for n in file1]
        file2 = [int(n.strip()) for n in file2]
        result = [n for n in file1 if n in file2]
        print(result)


# readsfile()
