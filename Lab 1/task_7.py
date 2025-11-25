t = int(input("Enter time in seconds: "))
minutes = t // 60
new_seconds = t - minutes * 60
print("Time: ",  minutes,  'm', new_seconds, 's')