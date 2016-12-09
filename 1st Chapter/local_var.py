
print('Local Variabe example')
def local():
    x = 10;
    print(x)
local()

print('Local Variabe example is not working  when it goes to other function or loop')


def notLocal():
    z = 10
    print( x + z )
notLocal()
    
