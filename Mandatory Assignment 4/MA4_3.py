from MA4_2 import fib_numba, fib_py
from person import Person
from numba import njit
from time import perf_counter
import matplotlib.pyplot as plt


def main():
    py_vec = [fib_py(i) for i in range(20, 31)]
    numba_vec = [fib_numba(i) for i in range(20, 31)]
    plt.figure()
    plt.plot(range(20, 31), py_vec, color="blue", label="Python")
    plt.plot(range(20, 31), numba_vec, color="yellow", label="Numba")
    plt.xlabel("n")
    plt.ylabel("Time")
    plt.title("Runtime of Fibonnaci function")
    plt.legend()
    plt.savefig("MA4_3fig")


if __name__ == "__main__":
    main()
