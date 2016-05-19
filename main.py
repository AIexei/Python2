from modules.xrange import *
from modules.vector import *
from modules.decorator import *
from collections import *
import time


d = {1: '3', 2: '4', 3:'5'}
for i in d.items():
    print(i[0])


#def my_fib(num):
#    if num == 1 or num == 2:
#        return 1
#    return my_fib(num - 1) + my_fib(num - 2)
#
#cache.clear()
#
#time.clock()
#
#start = time.clock()
#print(my_fib(33))
#print("Exec time is %.7f", time.clock()-start)
#
#start = time.clock()
#print(fib(10))
#print("Exec time is %.7f", time.clock()-start)
#
#print(cache)