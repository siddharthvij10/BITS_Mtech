import sys
import math
import numpy as np

from gauss_elimination_Q12 import *
from guass_elimination_Q13 import *
import time
import matplotlib.pyplot as plt


def make_graph(input_list, time_consumed_n_by_b_matrix):
    input_list = [math.log(i) for i in input_list]
    time_consumed_n_by_b_matrix = [math.log(i) for i in time_consumed_n_by_b_matrix]

    slope, _ = np.polyfit(input_list, time_consumed_n_by_b_matrix, 1)
    x = input_list
    y = time_consumed_n_by_b_matrix
    plt.plot(x, y)
    plt.show()
    return slope


def theoritical_time_consumption():
    pass

if __name__ == "__main__":

    choice = input("Enter 1 for GE without pivoting.\nEnter 2 for GE with pivoting.\n")
    choice = int(choice)
    print("you selected {} as your input choice".format(choice))

    list_of_matrix, list_of_R, list_or_C, start, end, step = generate_random_matrices()

    total_div = 0
    total_mul = 0
    total_add = 0
    time_consumed_n_by_b_matrix = []
    theoritical_time_consumed_n_by_b_matrix = []
    time_in_one_operation = 0.000000001

    for matrix, R, C in zip(list_of_matrix, list_of_R, list_or_C):

        start_time = time.time()

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

        fwd_elim_time = div_count_fwd + mul_count_fwd + add_count_fwd
        bwd_subs_time = mul_count_bwd + add_count_bwd + div_count_bwd
        end_time = time.time()
        time_consumed_n_by_b_matrix.append(end_time - start_time)
        theoritical_time_consumed_n_by_b_matrix.append(time_in_one_operation * (fwd_elim_time+bwd_subs_time))

    print('time_consumed is ', time_consumed_n_by_b_matrix)
    print('theoritical_time_consumed is ', theoritical_time_consumed_n_by_b_matrix)

    input_range = [i for i in range(start, end, step)]
    slope = make_graph(input_range, time_consumed_n_by_b_matrix)
    print("slope is ", slope)

