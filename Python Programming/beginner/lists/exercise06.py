list_numbers = []
sum_numbers = 0
product_numbers = 1

for x in range(1, 6):
    number = int(input("Number: "))
    list_numbers.append(number)


for x in list_numbers:
    sum_numbers = sum_numbers + x
    product_numbers *= number

print("Value of sum numbers is: %d" % sum_numbers)
print("Value of product numbers is: %d" % product_numbers)
