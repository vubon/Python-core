'''break is used inside for and while loops to alter their normal behavior.
break will end the smallest loop it is in and control flows to the statement
immediately below the loop. '''

for i in range(1, 10):
    if i == 5:
        break
    print(i)
