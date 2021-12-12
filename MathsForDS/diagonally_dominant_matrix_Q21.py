import numpy as np


def diagonally_dominant(matrix):
    print("input matrix is as follows:")
    print(matrix)
    diagonally_dominant_indicator = 1
    for row_num, row in enumerate(matrix):
        # print(row[row_num][row_num], 23)
        diagonal_element = abs(matrix[row_num][row_num])
        sum_non_diagonal_elements = 0
        for col_val in row:
            sum_non_diagonal_elements += abs(col_val)
        if diagonal_element > sum_non_diagonal_elements:
            continue
        else:
            diagonally_dominant_indicator = 0
            break

    return diagonally_dominant_indicator


def make_diagonally_dominant(matrix):
    indices_max_val_list = []
    for row_num, row in enumerate(matrix):
        row = np.absolute(row)
        indices_max_val_list.append(np.where(row == np.amax(row)))
    return indices_max_val_list


if __name__ == "__main__":
    # input matrix
    matrix =np.array ([[4, -3, 1],
              [-2, 1, -3],
              [-5, -10, 2]])

    diagonally_dominant_indicator = diagonally_dominant(matrix)
    if diagonally_dominant_indicator == 1:
        print("input matrix is diagonally dominant")
    else:
        print("input matrix is NOT diagonally dominant")
        indices_max_val_list = make_diagonally_dominant(matrix)
        if len(np.unique(indices_max_val_list)) == len(indices_max_val_list):
            print("the input matrix can be made diagonally dominant.")
        else:
            print("the input matrix can NOT be made diagonally dominant.")
