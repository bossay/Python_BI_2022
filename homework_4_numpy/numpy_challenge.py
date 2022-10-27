import numpy as np
# Create three of my favorite arrays.
if __name__ == "__main__":
    favorite_arr_1 = np.arange(5, 21, 2)
    favorite_arr_2 = np.random.randint(20, 35, size=(3, 3))
    favorite_arr_3 = (np.arange(1, 16)).reshape((3, 5))

# Matrix multiplication
def matrix_multiplication(matrix_1, matrix_2):
    return np.matmul(matrix_1, matrix_2)

# Matrix multiplication check
def multiplication_check(list_of_matrix):
    for i in range(len(list_of_matrix) - 1):
        if list_of_matrix[i].shape[1] == list_of_matrix[i+1].shape[0]:
            possibility = True
        else:
            possibility = False
    return possibility

# Multiplication of multiple matrices
def multiply_matrices(list_of_matrix):
    if multiplication_check(list_of_matrix):
        return np.linalg.multi_dot(list_of_matrix)
    else:
        return None

# Calculating the distance between two one-dimensional arrays
def compute_2d_distance(arr_1, arr_2):
    return np.linalg.norm(arr_1 - arr_2)

# Calculating distance between arrays
def compute_multidimensional_distanc(arr_1, arr_2):
    return np.linalg.norm(arr_1 - arr_2)

# Pairwise distance matrix
def compute_pair_distances(matrix):
    return np.linalg.norm(matrix[:, None] - matrix, axis=-1)