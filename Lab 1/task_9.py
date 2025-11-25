IP = input("Enter IP(XXX.XXX.XXX.XXX): ")
parts = IP.split('.')
if len(parts) != 4:
    print("IP is not correct. Must contain 4 parts.")
else:
    correct = True
    for part in parts:
        if not part.isdigit():
            correct = False
            break
        num = int(part)
        if num < 0 or num > 255:
            correct = False
            break
    if correct:
        print("IP is correct.")
    else:
        print("IP is not correct. ")