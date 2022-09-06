alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

def caesar(text, shift_amount, direction):
    end_text = ""
    if direction == "decode".lower():
        shift_amount *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here is the {direction} result {end_text}.")


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt. ")
    text = input("Type in you message. ")
    shift_amount = int(input("Type in the shift amount. "))
    caesar(text=text, shift_amount=shift_amount, direction=direction)

    restart = input("Type 'y' if you want to continue, or 'n' if you want to exit. ").lower()
    if restart == 'n':
        should_end = True
        print("Goodbye")
