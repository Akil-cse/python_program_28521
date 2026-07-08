char = input("Enter an alphabet character: ")
lower_char = char.lower()
if lower_char in ['a','e','i','o',"u"]:
    print(char, "is a vowel")
elif lower_char.isalpha():
    print (char, "is a consonant")
else:
    print("Invalid input! Please enter an alphabet")
