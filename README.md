import numpy as np

zeros_array = np.zeros(10)
fives_array = np.full(10, 5)
int_array = np.arange(10, 51)
even_array = np.arange(10, 51, 2)
matrix = np.arange(9).reshape(3, 3)
identity_matrix = np.eye(3)
random_num = np.random.rand()
random_array = np.random.rand(25)
linspace_array = np.linspace(0, 1, 20)
one_d_array = np.arange(10)
two_d_array = one_d_array.reshape(2, -1)

print("Zeros Array:", zeros_array)
print("Fives Array:", fives_array)
print("Integer Array (10-50):", int_array)
print("Even Array (10-50):", even_array)
print("3x3 Matrix:", matrix)
print("Identity Matrix:", identity_matrix)
print("Random Number:", random_num)
print("Random Array (25 elements):", random_array)
print("Linearly Spaced Array (0-1, 20 points):", linspace_array)
print("1D to 2D Array (2 rows):", two_d_array)
