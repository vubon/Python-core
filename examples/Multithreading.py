'''
Basic of Threading:
Threading remove lot of execute time. Let your machine a math in 20 seconds.
In this case if you use threading module if can save lot of time . such as half or less below .

let's complete a basic stuff of threading :)
'''
import time
import threading

def calc_square(numbers):
    print("Print Square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square: ", n^2 )
def calc_cube(numbers):
    print("Print Cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube numbers: ", n^3)


arr= [2,3,4,5]
t = time.time()

#calc_square(arr)
#calc_cube(arr)
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("It is done: ", time.time() - t)