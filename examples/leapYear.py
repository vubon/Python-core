year = int(input('Enter your year: ' ))
def is_leap(year):
    #leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(str(year) + ' is leap year')
    else:
        print(str(year) + ' is not leap year')

    #leap = True
    #return leap
print(is_leap(year))
