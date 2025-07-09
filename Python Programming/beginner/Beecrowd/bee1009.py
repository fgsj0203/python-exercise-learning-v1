name_employee = str(input("first name of employee: "))
salary_employee = float(input("Salary employee: "))
value_sold = float(input("Sold value of employee: "))
bonus_sold_value = value_sold * 0.15
# (optional) salary_final_bonus = salary_employee + bonus_sold_value
# (optional) print(salary_final_bonus)
print(
    "You value of bonus is %.2f and salary final with %.2f is %.2f "
    % (bonus_sold_value, salary_employee, bonus_sold_value + salary_employee)
)
