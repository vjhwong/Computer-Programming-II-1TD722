"""Uppgift 1.1"""
import random
import matplotlib.pyplot as plt
import numpy as np


def pi_approx(n):
    coordinates = []
    n_c = []
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        coordinates.append((x, y))
        if x**2 + y**2 <= 1:
            n_c.append((x, y))
        x_coordinates = [i[0] for i in coordinates]
        y_coordinates = [i[1] for i in coordinates]
        n_c_x = [i[0] for i in n_c]
        n_c_y = [i[1] for i in n_c]
    pi_approx = 4 * len(n_c) / len(coordinates)
    plt.scatter(x_coordinates, y_coordinates, color="blue", marker="o")
    plt.scatter(n_c_x, n_c_y, color="red", marker="o")
    plt.show()
    return pi_approx


""" def _pi_approx(n):
    coordinates, n_c = np.empty(n), np.empty(n)
    for i in range(n):
        coordinates = np.append(
            coordinates, np.array(random.uniform(-1, 1), random.uniform(-1, 1))
        )
        # coordinates[i] = (random.uniform(-1, 1), random.uniform(-1, 1))
        if np.sum(coordinates[i] ** 2) <= 1:
            n_c = np.append(n_c, coordinates[i])
    pi_approx = 4 * len(n_c) / len(coordinates)
    plt.scatter(coordinates[:, 0], coordinates[:, 1], color="blue", marker="o")
    plt.scatter(n_c[:, 0], n_c[:, 1], color="red", marker="o")
    plt.show()
    return pi_approx """


# n = [10000]
n = [1000, 10000]
pi_vec = []
for i in n:
    pi_vec.append(pi_approx(i))
print(pi_vec)
