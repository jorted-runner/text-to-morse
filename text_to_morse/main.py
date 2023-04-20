from morse_dict import morse_dict

converted_text = ''
morse_word = []
convert = True

print("\nText to Morse Code Converter\n\n")

while convert:
    user_text = input("Enter Text to be converted: ")
    if user_text == "QUIT":
        convert = False
    else:
        for letter in user_text.lower():
            if letter == " ":
                morse_word.append("    ")
            else:
                morse_word.append(f"{morse_dict[letter]}   ")

        print(converted_text.join(morse_word))