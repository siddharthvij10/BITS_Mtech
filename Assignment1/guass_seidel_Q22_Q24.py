import numpy as np
import math
import matplotlib.pyplot as plt

def generate_A_and_b_matrices_numpy():
    A = np.random.randn(4, 4)
    b = np.random.randn(1, 4)
    iteration_matrix = np.append(A, np.reshape(b, (-1, 1)), axis=1)
    return A, b, iteration_matrix


def calculate_vector_norm(iteration_matrix):
    iteration_matrix_for_comp = np.absolute(iteration_matrix)
    norm_1 = (iteration_matrix_for_comp.sum(axis=0))
    norm_1 = np.amax(norm_1)

    norm_inf = (iteration_matrix_for_comp.sum(axis=1))
    norm_inf = np.amax(norm_inf)

    norm_fro = 0
    for row in iteration_matrix_for_comp:
        for col in row:
            norm_fro += col**2
    norm_fro = math.sqrt(norm_fro)

    return norm_1, norm_inf, norm_fro


def guass_seidel(iteration_matrix, A, b):
    A = np.array([[12,3,-5], [1,5,3], [3,7,13]])
    b = np.array([1, 28, 76])
    print('input A is below')
    print(A)
    print('input b is below')
    print(b)
    rows_in_X = len(A)
    X = rows_in_X * [0]
    iterations = 10
    all_iteration_output = np.zeros(shape=(iterations, rows_in_X ))
    for iteration in range(iterations):
        for row_count, i in enumerate(A):

            temp_b = b[row_count]
            temp_a = A[row_count][row_count]
            temp_x = 0
            for col_count, j in enumerate(i):
                if col_count == row_count:
                    pass
                else:
                    temp_x = temp_x - (j*X[col_count])
            temp_x = temp_x + temp_b
            temp_x = temp_x/temp_a
            X[row_count] = temp_x
        all_iteration_output[iteration] = X
    print('guass seidel output for 10 iterations is below')
    print(all_iteration_output)

    x_new_minus_x_old = np.zeros(shape=(iterations-1, rows_in_X))
    X_temp = np.zeros(shape=(1, rows_in_X))
    for counter, iteration in enumerate(all_iteration_output):
        if counter == 0:
            X_temp = iteration
        else:
            x_new_minus_x_old[counter-1] = np.subtract(X_temp, iteration)
            X_temp = iteration

    print("new and old values difference over 10 iterations is below")
    print(x_new_minus_x_old)

    l2_vec_list = []
    for vec in x_new_minus_x_old:
        l2_vec = np.square(vec)
        l2_vec = np.sum(l2_vec)
        l2_vec = np.sqrt(l2_vec)
        l2_vec_list.append(l2_vec)
    print("l2 norm vector of new minus old value is below")
    print(l2_vec_list)


    x = [i for i in range(iterations-1)]
    y = l2_vec_list
    plt.plot(x, y)
    plt.show()


if __name__=="__main__":
    A, b, iteration_matrix = generate_A_and_b_matrices_numpy()
    norm_1, norm_inf, norm_fro = calculate_vector_norm(iteration_matrix)
    guass_seidel(iteration_matrix,A, b)
