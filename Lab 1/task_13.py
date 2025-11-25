import random
b = random.randint(1, 100)
a = -1
while a != b:
    a = int(input("Enter number(1-100): "))
    if a > b:
        print("Lower!")
    elif a < b:
        print("Higher!")
    else:
        print("Correct number!")