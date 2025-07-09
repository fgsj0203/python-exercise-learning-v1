list_numbers = []
sum_numbers = 0


for x in range(0, 10):
    number = int(input("Number: "))
    list_numbers.append(number)
    sum_numbers += list_numbers[x] ** 2

print("List of numbers is: ", list_numbers)
print("Sum of all numbers elevate of square is: ", sum_numbers)
