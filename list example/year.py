from random import randint
def random_with(n):
    range_start =1000  #10**(n-1)
    range_end = 9000 #(10**n)-1
    return randint(range_start, range_end)
print(random_with(4))

'''
year = range(1000,9000)
year = input('Enter your year: ')
if len(year)== 4 and year.isdigit():
    for i in range(4):
        a = year[random.randint(0, len(year)-i)]
        year.remove(year)
        print(a)
else:
    print('it must over 4 digits. ')

'''

