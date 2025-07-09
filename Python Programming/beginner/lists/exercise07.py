"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
"""

age_list = []
height_list = []

for x in range(0, 5):
    age = int(input("Age of people: "))
    height = float(input("Height people: "))
    age_list.append(age)
    height_list.append(height)

print("List of age people in order original: ", age_list)
print("List of height people in order original: ", height_list)
print("List of age in order reverse: ", age_list[::-1])
print("List of height in order reverse: ", height_list[::-1])
