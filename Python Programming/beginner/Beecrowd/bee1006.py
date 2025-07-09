number_a = float(input("number A: "))
while number_a > 10 or number_a < 0:
    print("Try again with number A!!")
    number_a = float(input("number a: "))

number_b = float(input("number B: "))
while number_b > 10 or number_b < 0:
    print("Try again with number B")
    number_b = float(input("number b: "))

number_c = float(input("number C: "))
while number_c > 10 or number_c < 0:
    print("Try again with number C")
    number_c = float(input("number c: "))

average_calculate = (number_a * 2.0 + number_b * 3.0 + number_c * 5.0) / (
    2.0 + 3.0 + 5.0
)

print("Average: %.1f " % average_calculate)
