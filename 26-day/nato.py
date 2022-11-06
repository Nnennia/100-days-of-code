# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("26-day/nato_phonetic_alphabet.csv")

new_data = {row.letter: row.code for (index, row) in data.iterrows()}

# print(new_data)
word = input("Input a word: ").upper()

list_word = [new_data[letter] for letter in word]

print(list_word)
