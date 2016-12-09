'''
actually zip function is making all list files together and print too .
'''

one = [1, 2, 3, 4, 5]
two = [6, 7, 8, 9, 10]
total = zip(one, two)
for a, b in total:
    print(a, b)

