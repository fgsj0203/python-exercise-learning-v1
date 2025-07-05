letter = str(input("Letter: "))
letter_lower = letter[0].lower()

if (
    letter_lower != "a"
    and letter_lower != "e"
    and letter_lower != "i"
    and letter_lower != "o"
    and letter_lower != "u"
):
    print("Letter is consonant")
else:
    print("Letter is vowel")
