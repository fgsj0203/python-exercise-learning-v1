list_number_pair = []
list_number_odd = []
count_number_pair = 0
count_number_odd = 0
for x in range(0, 9):
    number = int(input("Number: "))
    if number % 2 == 0:
        print("Number pair")
        list_number_pair.append(number)
        count_number_pair += 1
    else:
        print("Number odd")
        list_number_odd.append(number)
        count_number_odd += 1


print("Count numbers pair: %d" % count_number_pair)
print("Count numbers odd: %d" % count_number_odd)
print("List of numbers pair: ", list_number_pair)
print("List of numbers odd: ", list_number_odd)
