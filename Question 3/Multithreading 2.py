import time
import timeit
import threading as thr

from Factorial import factorial

import sys, sysconfig

# print(sys.version)
# print(sys._is_gil_enabled())  # returns False when GIL is disabled
# print(sysconfig.get_config_var("Py_GIL_DISABLED"))  # 1 if free-threading support is enabled


def multithread():
    t1 = thr.Thread(target=factorial, args=(50,))
    t2 = thr.Thread(target=factorial, args=(100,))
    t3 = thr.Thread(target=factorial, args=(200,))

    threads = [t1, t2, t3]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def single_thread():
    factorial(50)
    factorial(100)
    factorial(200)

if __name__=="__main__":
    print('*****Multithreading*****')
    duration = timeit.timeit(multithread,number=1000)
    print(duration)

    print('')
    print('*****Singlethreading*****')
    duration = timeit.timeit(single_thread,number=1000)
    print(duration)