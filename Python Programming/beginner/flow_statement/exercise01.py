note = int(input("Enter with you note: "))

while note < 0 or note > 10:
    print("Note invalid, try again!!")
    note = int(input("Enter with you note: "))

print("Number final is: %d " % note)
