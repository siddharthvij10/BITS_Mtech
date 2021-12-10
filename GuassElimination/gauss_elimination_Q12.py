"""Write a function to implement Gauss elimination with and without pivoting. Also write the code to count the number
of additions, multiplications and divisions performed during Gaussian elimination. Ensure that the Gauss elimination
performs 5S arithmetic which necessitates 5S arithmetic rounding for every addition, multiplication and division
performed in the algorithm. If this is not implemented correctly, the rest of the answers will be considered invalid.
Note that this is not same as simple 5 digit rounding at the end of the computation. Do not hardwire 5S arithmetic in
the code and use dS instead. The code can then be run with various values of d."""
import sys
import numpy as np
import math


def print_matrix(R, C, matrix):
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end=" ")
        print()


def forward_elimination(R, C, matrix):
    div_count = 0
    mul_count = 0  # the cell which we are making 0 and column before that is not counted in this factor.
    add_count = 0
    for box in range(C):
        for i in range(box, R - 1):
            div_factor = matrix[i + 1][box] / matrix[box][box]
            div_factor = rounding_sig_digits(div_factor, 5)
            div_count += 1
            for j in range(C):
                multiply_item_rounded = div_factor * matrix[box][j]
                multiply_item_rounded = rounding_sig_digits(multiply_item_rounded, 5)
                matrix[i + 1][j] = rounding_sig_digits((matrix[i + 1][j] - multiply_item_rounded), 5)
                if j > box:
                    mul_count += 1
                    add_count += 1
                else:
                    pass
    pass
    print("matrix after forward elimination is as follows:")
    print_matrix(R, C, matrix)

    return matrix, div_count, mul_count, add_count


def forward_elimination_pivot(R, C, matrix):
    div_count = 0
    mul_count = 0  # the cell which we are making 0 and column before that is not counted in this factor.
    add_count = 0
    for box in range(C):
        if box == C - 1:
            pass
        else:
            max = matrix[box][box]
            max_row = max_row_initial = box
            max_row_val_initial = list(matrix[max_row_initial])
            pivot_indicator = 0

            for i in range(box, R):
                if abs(matrix[i][box]) > max:
                    max = matrix[i][box]
                    max_row = i
                    pivot_indicator = 1
            if pivot_indicator == 0:
                pass
                print("no pivoting in this box. matrix is")
                print_matrix(R,C,matrix)
            else:
                # print("pivoting required. before pivoting")
                # print_matrix(R,C,matrix)
                for col, val in enumerate(matrix[max_row]):
                    matrix[max_row_initial][col] = val
                for col, val in enumerate(max_row_val_initial):
                    matrix[max_row][col] = val
                print("pivoting required. after pivoting")
                print_matrix(R, C, matrix)
        for i in range(box, R - 1):
            div_factor = matrix[i + 1][box] / matrix[box][box]
            div_factor = rounding_sig_digits(div_factor, 5)
            print('rounded div factor is ', div_factor)
            div_count += 1

            for j in range(C):
                multiply_item_rounded = div_factor * matrix[box][j]
                multiply_item_rounded = rounding_sig_digits(multiply_item_rounded, 5)
                print('multiply_item_rounded is ', multiply_item_rounded)
                matrix[i + 1][j] = rounding_sig_digits((matrix[i + 1][j] - multiply_item_rounded), 5)
                if j > box:
                    mul_count += 1
                    add_count += 1
                else:
                    pass

    pass
    print("matrix after forward elimination with pivoting is as follows:")
    print_matrix(R,C,matrix)
    return matrix, div_count, mul_count, add_count


def verify_unique_sol(R, C, matrix):

    input_matrix = matrix
    counter_temp = 0
    rank_input_matrix = 0
    for row in input_matrix:
        if counter_temp == 0:
            no_of_unknowns = len(row)
            counter_temp += 1
        if any(row):
            rank_input_matrix += 1
        else:
            pass

    b = []
    A = tuple()
    a = []
    for i in range(R):
        for j in range(C):
            if j == C-1:
                b.append(matrix[i][j])
            else:
                a.append(matrix[i][j])
        A += (a,)
        a = []

    rank_b = 0
    for i in b:
        if i != 0:
            rank_b += 1

    counter_temp = 0
    rank_a = 0
    for row in A:
        if counter_temp == 0:
            no_of_unknowns = len(row)
            counter_temp += 1
        if any(row):
            rank_a += 1
        else:
            pass

    if rank_b != rank_a:
        print('unique sol does not exist')
        sys.exit()
    else:
        pass

    no_of_equations = rank_input_matrix
    if no_of_equations != no_of_unknowns:
        print('unique sol does not exist')
        sys.exit()
    else:
        pass
    return no_of_unknowns


def backward_substitution(R, C, matrix, no_of_unknowns):

    div_count = 0
    mul_count = 0
    add_count = 0

    m = matrix
    X = [0] * no_of_unknowns
    N = C-1
    for n, k in zip(range((R-1), -1, -1), range(0, R)):
        numerator = m[n][N]
        denominator = m[n][n]
        while k > 0:
            numerator = rounding_sig_digits((numerator - rounding_sig_digits((m[n][n+k] * X[n+k]), 5)), 5)
            add_count += 1
            mul_count += 1
            k-=1
        X[n] = rounding_sig_digits(numerator/denominator, 5)
        div_count += 1
    pass
    print('solution of linear system as a vector X containing X1, X2 .. XN is ', X)
    return div_count, mul_count, add_count


def rounding_sig_digits(N, n):  # N is input number, n is sig digits
    if N != 0:
        f = int(math.floor(math.log10(abs(N))))
        f = n-f-1
        j = round(N, f)
    else:
        j = N
    return j


if __name__ == "__main__":

    # input matrix
    matrix = ([4, -3, 1, -8],
              [-2, 1, -3, -4],
              [-5, -1, 2, 3])
    R, C = 3, 4

    choice = input("Enter 1 for GE without pivoting.\nEnter 2 for GE with pivoting.\n")
    choice = int(choice)
    print("you selected {} as your input choice".format(choice))

    print('matrix in input is as follows:')
    print_matrix(R,C,matrix)

    if choice == 1:
        matrix_upper_triangular, div_count_fwd, mul_count_fwd, add_count_fwd = forward_elimination(R, C, matrix)
    else:
        matrix_upper_triangular, div_count_fwd, mul_count_fwd, add_count_fwd = forward_elimination_pivot(R, C, matrix)

    # pass
    print("operation counts in forward elimination div_count is {}, mul_count is {} and add_count is {}".format(div_count_fwd, mul_count_fwd, add_count_fwd))

    no_of_unknowns = verify_unique_sol(R, C, matrix_upper_triangular)

    matrix_upper_triangular = np.asarray(matrix_upper_triangular)

    div_count_bwd, mul_count_bwd, add_count_bwd = backward_substitution(R, C, matrix_upper_triangular, no_of_unknowns)
    # pass
    print("operation counts in backward substitution for div_count is {}, mul_count is {} and add_count is {}".format(div_count_bwd, mul_count_bwd, add_count_bwd))

    print("total operations for division is {}, multiplication is {} and addition is {}".format((div_count_bwd +div_count_fwd)
                                                                                                ,(mul_count_fwd + mul_count_bwd)
                                                                                                ,(add_count_fwd + add_count_bwd)))
