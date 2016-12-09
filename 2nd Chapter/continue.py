'''Continue is used inside for and while loops to alter their normal behavior.
Continue will end the smallest loop it is in and control flows to the statement
immediately below the loop. '''

for i in range(1, 11):
    if i == 6:
        continue
    print(i)
