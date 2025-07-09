name_user = str(input("Enter with name user: "))
password = str(input("Enter with you password: "))

while name_user == password:
    print("Name user is equal password, try again!!")
    name_user = str(input("Name user: "))
    password = str(input("Password: "))

print("You name user is: %s" % name_user)
print("You password is: %s" % password)
