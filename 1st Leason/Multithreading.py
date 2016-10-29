import time
import threading
def calc_square(numbers):
    print("Calculate squares numbers")
    for v in numbers:
        time.sleep(0.2)
        print("Square: ", v *v )

def calc_cube(numbers):
    print("Calculate cube numbers")
    for v in numbers:
        time.sleep(0.2)
        print("Cube: ", v *v *v )

arr=[2,3,4,5,6,7,8,9]
t = time.time()

#calc_square(arr)
#calc_cube(arr)
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print("Done it: ", time.time() - t)

