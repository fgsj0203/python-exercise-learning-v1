salary_employee = float(input("your salary: "))

if salary_employee <= 200:
    growth_salary = salary_employee + (salary_employee * 0.20)
elif salary_employee <= 700:
    growth_salary = salary_employee + (salary_employee * 0.25)
elif salary_employee <= 1500:
    growth_salary = salary_employee + (salary_employee * 0.10)
else:
    growth_salary = salary_employee + (salary_employee * 0.05)

print("Salary brute: %.2f" % salary_employee)
print("Value of growth salary: %.2f" % (growth_salary - salary_employee))
print("Value final with growth salary: %.2f" % growth_salary)
