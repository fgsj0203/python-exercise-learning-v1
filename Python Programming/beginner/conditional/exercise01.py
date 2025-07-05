"""
Author: Francisco Gomes da Silva Junior
Source: statements flow - https://github.com/selatotal/pythonBrasilExercicios/tree/master/02_EstruturasDecisao
Date: 04/07/2025 - format Brazil
Version: 1.0
"""

number_one = int(input("number one: "))
number_two = int(input("number two: "))

if number_one > number_two:
    print("bigger = %d " % number_one)
elif number_two > number_one:
    print("bigger = %d" % number_two)
else:
    print("numbers is equals")
