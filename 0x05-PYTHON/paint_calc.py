def paint_calc(height,width,cover):
    number_can =round((test_h * test_w) / coverage)
    print(f"You will need {number_can} number of paints")

# import math
# math.ceil to round a number up to nearest whole number
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
