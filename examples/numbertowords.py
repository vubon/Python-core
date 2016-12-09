from num2words import num2words as number
first = int(input('Enter your first number: '))
second = int(input('Enter your second number: '))
for i in range(first, second):
    print(number(i))
