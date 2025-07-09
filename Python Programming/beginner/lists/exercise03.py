list_notes = []
sum_notes = 0
average_note = 0

for x in range(0, 4):
    note = float(input("Note: "))
    sum_notes += note
    list_notes.append(note)

average_note = sum_notes / 4

print("Average of notes is: %.2f " % average_note)
print("Notes: ", list_notes)
