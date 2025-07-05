gender = str(input("Gender: "))
first_letter_gender = gender[0]

if first_letter_gender.lower() == "m":
    print("Male")
elif first_letter_gender.lower() == "f":
    print("Female")
else:
    print("Gender invalid")
