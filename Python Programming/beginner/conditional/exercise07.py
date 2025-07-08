hours_worked_month = int(input("hours worked in month: "))
value_hour_worked = float(input("Value received for hour worked: "))

salary_brute = hours_worked_month * value_hour_worked

# Calculating values of discounts and increament FGTS
if salary_brute <= 900:
    print("Your salary is isent of tax")
elif salary_brute <= 1500:
    discount_value_ir = salary_brute * 0.05
elif salary_brute <= 2500:
    discount_value_ir = salary_brute * 0.10
else:
    discount_value_ir = salary_brute * 0.20

# Calculating increament value of FGTS
value_increament_fgts = salary_brute * 0.11

# Calculating discount of value INSS
value_discount_inss = salary_brute * 0.10

print("Your salary brute is: %.2f " % salary_brute)
print("Value of discount tax IR: %.2f " % discount_value_ir)
print("Value of discount tax INSS: %.2f " % value_discount_inss)
print("Value of increament FGTS: %.2f " % value_increament_fgts)
print("Value of total discounts: R$ %.2f" % ((discount_value_ir + value_discount_inss)))
print(
    "Salary liquid: R$ %.2f "
    % (salary_brute - (discount_value_ir + value_discount_inss))
)
