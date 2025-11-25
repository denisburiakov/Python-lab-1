
my_string = input("Enter string: ")

k = 'aieuoAIEUO'

result = ""
for i in my_string:
    if i  not in k:
        result += i
print('Result: ' + result)