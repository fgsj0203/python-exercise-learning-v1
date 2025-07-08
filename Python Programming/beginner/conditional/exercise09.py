note_one = float(input("Note one: "))
note_two = float(input("Note two: "))
average_notes = (note_one + note_two) / 2

print("You average notes is: %.2f " % average_notes)

if average_notes > 9.0 and average_notes <= 10.0:
    print("Concept A")
    print("Approved")
elif average_notes > 7.5 and average_notes <= 9.0:
    print("Concept B")
    print("Approved")
elif average_notes > 6.0 and average_notes <= 7.5:
    print("Concept C")
    print("Approved")
elif average_notes > 4.0 and average_notes <= 6.0:
    print("Concept D")
    print("Reproved")
else:
    print("Concept E")
    print("Reproved")
