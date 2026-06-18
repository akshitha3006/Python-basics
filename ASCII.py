user_input = input("Enter a single character: ")
ascii_value = ord(user_input)
print("The ASCII value of the character", user_input, "is", ascii_value)

if 'A' <= user_input <= 'Z':
    print("The character is an uppercase letter.")
elif 'a' <= user_input <= 'z':
    print("The character is a lowercase letter.")
elif '0' <= user_input <= '9':
    print("The character is a digit.")
else:
    print("The character is a special character.")    