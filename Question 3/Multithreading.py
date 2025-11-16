import time
import threading as thr

from Factorial import factorial

# import sys, sysconfig

# print(sys.version)
# print(sys._is_gil_enabled())  # returns False when GIL is disabled
# print(sysconfig.get_config_var("Py_GIL_DISABLED"))  # 1 if free-threading support is enabled


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
    m_times = []
    for i in range(11):
        time_taken = multithread()
        if i>0:
            print(f"Iteration {i} complete. Time taken: {time_taken} nanoseconds")
            avg_time_m += time_taken
            m_times.append(time_taken)
        else:
            print(f"Warm up complete. Time taken: {time_taken} nanoseconds")
    avg_time_m /= 10
    print(
        f"10 iterations complete.\n"
        f"Total time taken: {avg_time_m*10} nanoseconds\n"
        f"Average time taken: {avg_time_m} nanoseconds"
    )

    print('\n*****Singlethreading*****')
    avg_time_s = 0
    s_times = []
    for i in range(11):
        time_taken = single_thread()
        if i>0:
            print(f"Iteration {i} complete. Time taken: {time_taken} nanoseconds")
            avg_time_s += time_taken
            s_times.append(time_taken)
        else:
            print(f"Warm up complete. Time taken: {time_taken} nanoseconds")
    avg_time_s /= 10
    print(
        f"10 iterations complete.\n"
        f"Total time taken: {avg_time_s * 10} nanoseconds\n"
        f"Average time taken: {avg_time_s} nanoseconds"
    )

    if avg_time_s < avg_time_m:
        winner = "Singlethreading"
        loser = "Multithreading"
        win_count = sum(1 if a > b else 0 for a, b in zip(m_times, s_times))
    else:
        winner = "Multithreading"
        loser = "Singlethreading"
        win_count = sum(1 if a > b else 0 for a, b in zip(s_times, m_times))

    print('')
    print(f"{winner} is faster than {loser}")
    print(f"{winner} beats {loser} in {win_count}/10 iterations")
    print(f"Time difference: {abs(avg_time_s-avg_time_m)}")