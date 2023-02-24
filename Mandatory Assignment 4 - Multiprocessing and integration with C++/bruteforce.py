"""Uppgift 1.3"""
from time import perf_counter as pc
from ndimspherevolume import vol_sim


def main():
    start = pc()

    result = vol_sim(11, 10000000)
    print(result)

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")
    # result = 1.8917376
    # Took 78.1 seconds


if __name__ == "__main__":
    main()
