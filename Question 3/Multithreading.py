import time
import threading as thr

from Factorial import factorial

def wait_2():
    time.sleep(2)

def multithread():
    t1 = thr.Thread(target=factorial, args=(50,))
    t2 = thr.Thread(target=factorial, args=(100,))
    t3 = thr.Thread(target=factorial, args=(200,))

    threads = [t1, t2, t3]

    start_time = time.perf_counter_ns()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter_ns()

    return end_time-start_time

def single_thread():
    start_time = time.perf_counter_ns()

    factorial(50)
    factorial(100)
    factorial(200)

    end_time = time.perf_counter_ns()

    return end_time - start_time

if __name__=="__main__":
    print('*****Multithreading*****')
    avg_time_m = 0
    for i in range(10):
        time_taken = multithread()
        print(f"Iteration {i+1} complete. Time taken: {time_taken} nanoseconds")
        avg_time_m += time_taken
    avg_time_m /= 10
    print(f"10 iterations complete. Average time taken: {avg_time_m} nanoseconds")

    print('\n*****Singlethreading*****')
    avg_time_s = 0
    for i in range(10):
        time_taken = single_thread()
        print(f"Iteration {i + 1} complete. Time taken: {time_taken} nanoseconds")
        avg_time_s += time_taken
    avg_time_s /= 10
    print(f"10 iterations complete. Average time taken: {avg_time_s} nanoseconds")

    winner = "\nSinglethreading" if avg_time_s<avg_time_m else "Multithreading"
    loser = "Singlethreading" if avg_time_s>=avg_time_m else "Multithreading"
    print(f"{winner} is faster than {loser}")
    print(f"Time difference: {abs(avg_time_s-avg_time_m)}")