note_one = float(input("note one: "))
note_two = float(input("note two: "))
average_notes = (note_one + note_two) / 2

if average_notes == 10.0:
    print("Approved with distinction")
elif average_notes >= 7.0 and average_notes <= 9.9:
    print("Approved")
else:
    print("Reproved")

# -----------------------------------------------------------
# Second method with validation value
note_one = float(input("note one: "))
while note_one < 0 or note_one > 10:
    print("Note invalid, try again!!")
    note_one = float(input("Note one: "))

note_two = float(input("note two: "))
while note_two < 0 or note_two > 10:
    print("Note invalid, try again!!")
    note_two = float(input("Note one: "))

average_notes = (note_one + note_two) / 2

if average_notes == 10.0:
    print("Approved with distinction")
elif average_notes >= 7.0 and average_notes <= 9.9:
    print("Approved")
else:
    print("Reproved")
