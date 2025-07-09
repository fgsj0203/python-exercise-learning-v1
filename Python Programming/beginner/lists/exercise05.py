list_numbers_all = []
list_numbers_pair = []
list_numbers_odd = []

for x in range(0, 10):
    number = int(input("Number: "))

    list_numbers_all.append(number)
    if number % 2 == 0:
        list_numbers_pair.append(number)
    else:
        list_numbers_odd.append(number)


print("list of all numbers: ", list_numbers_all)
print("list of numbers pair: ", list_numbers_pair)
print("list of numbers odd: ", list_numbers_odd)
