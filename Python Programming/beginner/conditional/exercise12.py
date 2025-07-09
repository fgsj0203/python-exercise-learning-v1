print("Awsner questions - criminal ")

count_classified_criminal = 0

question_one = str(input("Cellphone for victim?"))
if question_one == "y":
    count_classified_criminal += 1

question_two = str(input("You in local criminal?"))
if question_two == "y":
    count_classified_criminal += 1

question_three = str(input("Living with victim?"))
if question_three == "y":
    count_classified_criminal += 1

question_four = str(input("You money for victim?"))
if question_four == "y":
    count_classified_criminal += 1

question_five = str(input("You worked for victim? "))
if question_five == "y":
    count_classified_criminal += 1

if count_classified_criminal <= 2:
    print("Suspect")
elif count_classified_criminal <= 4:
    print("Cumplice")
elif count_classified_criminal == 5:
    print("You Assassin!")
else:
    print("You is inocent!")
