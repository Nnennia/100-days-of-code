alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
	cipher_text = ""
	for letter in plain_text:
		position = alphabet.index(letter)
		new_position = position + shift_amount
		new_letter = alphabet[new_position]
		cipher_text += new_letter

	print(f"The encoded text is {cipher_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(index_text,shift_number):
	cipher_text = ""
	for letter in index_text:
		position = alphabet.index(letter)
		new_position = position - shift_number
		new_letter = alphabet[new_position]
		cipher_text += new_letter

	print(f"The decoded text is {cipher_text}")

if direction == "encode":
	encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
	decrypt(index_text = text, shift_number=shift)
