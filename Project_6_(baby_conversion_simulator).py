from random import choice

Questions=["Why is Sky blue in colour ? :","Why do sun and moon do not meet ? : ","Why do people have name ? :"]

Question=choice(Questions)

answer=input(Question).strip().lower()

while answer!="Just because" :

    answer=input("Why :")

print("Oh.....ok")
