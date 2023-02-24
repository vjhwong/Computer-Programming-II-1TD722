#!/usr/bin/env python3.9
# Graded by: Sergi Olives Juan
# 26 september 2022
from person import Person
from numba import njit
from time import perf_counter
import matplotlib.pyplot as plt


def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n - 1) + fib_py(n - 2)


@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n - 1) + fib_numba(n - 2)


def main():
    p = Person(10)
    sizes = [i for i in range(30, 40)]
    runtime_cpp, runtime_py, runtime_numba = [], [], []

    print(p.fib())  # C++: -1323752223
    print(fib_numba(10))


"""     for n in sizes:
        # C++ time
        p.set(n)
        t_start_cpp = perf_counter()
        p.fib()
        t_stopp_cpp = perf_counter()
        runtime_cpp.append(t_stopp_cpp - t_start_cpp)

        # Python time
        t_start_py = perf_counter()
        fib_py(n)
        t_stopp_py = perf_counter()
        runtime_py.append(t_stopp_py - t_start_py)

        # numba time
        t_start_numba = perf_counter()
        fib_numba(n)
        t_stopp_numba = perf_counter()
        runtime_numba.append(t_stopp_numba - t_start_numba) """


""" 
    plt.figure()

    plt.plot(sizes, runtime_cpp, color="green", label="C++")
    plt.plot(sizes, runtime_py, color="blue", label="Python")
    plt.plot(sizes, runtime_numba, color="yellow", label="numba")

    plt.xlabel("n")
    plt.ylabel("Time")
    plt.title("Runtime of Fibonnaci function")
    plt.legend()
    plt.savefig("MA4_2fig")

    py_vec, numba_vec = [], []
    for i in range(20, 31):
        py_start = perf_counter()
        fib_py(i)
        py_stopp = perf_counter()
        py_vec.append(py_stopp - py_start)

        numba_start = perf_counter()
        fib_numba(i)
        numba_stopp = perf_counter()
        numba_vec.append(numba_stopp - numba_start)

    plt.figure()
    plt.plot(range(20, 31), py_vec, color="blue", label="Python")
    plt.plot(range(20, 31), numba_vec, color="yellow", label="Numba")
    plt.xlabel("n")
    plt.ylabel("Time")
    plt.title("Runtime of Fibonnaci function")
    plt.legend()
    plt.savefig("MA4_3fig")

 """
if __name__ == "__main__":
    main()
