id_employee = int(input("ID Employee: "))
work_hours_month = int(input("Hours worked in month: "))
value_receive_hour_work = float(input("Value of work receive for houe: $"))

salary_brute = work_hours_month * value_receive_hour_work
print("ID Employee: %d " % id_employee)
print("Salary brute = U$ %.2f" % salary_brute)
