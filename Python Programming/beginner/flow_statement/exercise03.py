# Validation of size name
name = str(input("Enter with name: "))
len_name = len(name)  # Size of name

while len_name <= 3:
    print("Try again, size of name is bigger 3 character")
    name = str(input("Enter with name: "))
    len_name = len(name)

print("----------------------------------------------------")

# Validation of age people
age_people = int(input("Enter with age: "))

while age_people < 0 or age_people > 150:
    print("Try again, you age is between 0 and 150")
    age_people = int(input("Age people: "))

print("----------------------------------------------------")
# Validation salary
salary = float(input("Enter with salary: "))

while salary < 0:
    print("Try again, salary is bigger of value 0")
    salary = float(input("Salary: "))
print("----------------------------------------------------")


# Validation gender
gender = str(input("Your gender: "))
gender_lower = gender[0].lower()

while gender_lower != "f" and gender_lower != "m":
    print("Try again! gender is m or f")
    gender = str(input("Gender: "))
    gender_lower = gender[0].lower()

print("----------------------------------------------------")

# Validation state civil
state_civil = str(input("You state civil: "))
lower_state_civil = state_civil[0].lower()

while (
    lower_state_civil != "s"
    and lower_state_civil != "c"
    and lower_state_civil != "v"
    and lower_state_civil != "d"
):
    print("Try again!")
    state_civil = str(input("You state civil: "))
    lower_state_civil = state_civil[0].lower()
print("----------------------------------------------------")

print(name)
print(age_people)
print(salary)
print(gender)
print(state_civil)
