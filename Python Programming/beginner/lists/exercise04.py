list_consonants = []
amount_consonants = 0

for x in range(0, 10):
    letter = str(input("Letter: "))
    if (
        letter != "a"
        and letter != "e"
        and letter != "i"
        and letter != "o"
        and letter != "u"
    ):
        list_consonants.append(letter)
        amount_consonants += 1

print("List of letters consonants: ", list_consonants)
print("Amount letters in consonante %d" % amount_consonants)
