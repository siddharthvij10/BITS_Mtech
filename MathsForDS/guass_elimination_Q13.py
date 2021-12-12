import sys

import numpy as np

from gauss_elimination_Q12 import *


def rounding_element_array(element):
    element = rounding_sig_digits(element, 5)
    return element


def generate_random_matrices(start, end, step):
    list_of_arrays = []
    list_of_matrix = []
    list_of_R = []
    list_of_C = []
    # start = 10
    # end = 21
    # step = 10
    for n in range(start, end, step):
        array = np.random.uniform(1, 10, (n, n))
        b = np.random.uniform(1, 10, n)
        array = np.append(array, np.reshape(b, (-1, 1)), axis=1)
        list_of_R.append(n)
        list_of_C.append(n+1)
        rounding_array = np.vectorize(rounding_element_array)
        array = rounding_array(array)
        array_of_tuples = map(list, array)
        tuple_of_lists = tuple(array_of_tuples)
        list_of_matrix.append(tuple_of_lists)
        list_of_arrays.append(array)
    return list_of_matrix, list_of_R, list_of_C, start, end, step


if __name__ == "__main__":

    choice = input("Enter 1 for GE without pivoting.\nEnter 2 for GE with pivoting.\n")
    choice = int(choice)
    print("you selected {} as your input choice".format(choice))

    list_of_matrix, list_of_R, list_or_C, _, _, _ = generate_random_matrices(10, 21, 10)

    total_div = 0
    total_mul = 0
    total_add = 0
    for matrix, R, C in zip(list_of_matrix, list_of_R, list_or_C):

        print('\nmatrix in input is as follows:')
        # matrix = ([9.9295, 8.0181, 4.941, 2.4063 ,1.3374],
        #             [1.8197, 4.9054, 9.3446 ,6.607 ,6.3052],
        #             [2.5673 ,8.1717, 8.9829 ,2.9926 ,5.3818],
        #             [5.4592 ,7.4433, 5.7872 ,9.3453 ,4.6737])
        # # R, C = 3, 4
        print_matrix(R,C,matrix)

        if choice == 1:
            matrix_upper_triangular, div_count_fwd, mul_count_fwd, add_count_fwd = forward_elimination(R, C, matrix)
        else:
            matrix_upper_triangular, div_count_fwd, mul_count_fwd, add_count_fwd = forward_elimination_pivot(R, C, matrix)
        print("operation counts in forward elimination div_count is {}, mul_count is {} and add_count is {}".format(div_count_fwd, mul_count_fwd, add_count_fwd))

        no_of_unknowns = verify_unique_sol(R, C, matrix_upper_triangular)

        matrix_upper_triangular = np.asarray(matrix_upper_triangular)

        div_count_bwd, mul_count_bwd, add_count_bwd = backward_substitution(R, C, matrix_upper_triangular, no_of_unknowns)
        print("operation counts in backward substitution for div_count is {}, mul_count is {} and add_count is {}".format(div_count_bwd, mul_count_bwd, add_count_bwd))

        print("total operations for R {} for division is {}, multiplication is {} and addition is {}".format(R
                                                                                                    ,(div_count_bwd +div_count_fwd)
                                                                                                    ,(mul_count_fwd + mul_count_bwd)
                                                                                                    ,(add_count_fwd + add_count_bwd)))

