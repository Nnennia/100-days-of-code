sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
new_sen = sentence.split()
lists = [len(word) for word in new_sen]
result = dict(zip(new_sen, lists))
print(result)

result = {word: len(word) for word in sentence.split()}
print(result)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
weather_f = {value: weather_c[value] * 9/5 + 35 for value in weather_c}

# {day:(temp_c*9/5) + 35 for (day, temp_c) in weather_c.items()}

print(weather_f)


# for (index, row) in stud_data.iterrows()
