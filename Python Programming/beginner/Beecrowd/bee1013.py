three_values = input().split()  # Converting values in list of type data "String"
value_one = int(three_values[0])  # casting value string for type data "int"
value_two = int(three_values[1])  # casting value string for type data "int"
value_three = int(three_values[2])  # casting value string for type data "int"

biggerAB = (value_one + value_two + abs(value_one - value_two)) / 2
bigger_final = (biggerAB + value_three + abs(biggerAB - value_three)) / 2

print(bigger_final)
