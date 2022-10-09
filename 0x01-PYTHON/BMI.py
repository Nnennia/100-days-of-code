# calculates BMI
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h = float(height) * float(height)
w = int(weight)
BMI = int(w/h)  # prints only whole numbers
print(BMI)

# or
BMI = int(weight) / float(height) ** 2
BMIm = int(BMI)
print(BMIm)
