print('Program is starting')
#ask a question
israining= input('Is raining?:' )
yes = str('yes')
no = str('no')
outside = str('Go outside')
if israining == yes:
    haveumbrella=input('Have umbrella?: ' )
    if haveumbrella == yes:
        print(outside)
    else:
        print('Wait a while')
        israining = input('Is a raining?: ')
        if israining == yes:
            print('Wait a while')
        else:
            print(outside)
else:
    print(outside)
