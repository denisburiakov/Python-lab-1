o = int(input("Enter number: "))
if o % 7 == 0:
    print("Magic number!")
else:

    sum_of_digits = 0
    temp = abs(o)
    while temp > 0:
        sum_of_digits += temp % 10
        temp //= 10
    print(sum_of_digits)
