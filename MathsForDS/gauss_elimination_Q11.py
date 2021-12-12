"""Find the approximate time your computer takes for a single addition by adding first 10 ** 6 positive integers
using a for loop and dividing the time taken by 10 ** 6. Similarly find the approximate time taken for a
single multiplication and division. Report the result obtained in the form of a table."""

import time


def addition(i):

    start_time = time.time()

    sum_var = 0
    for no in range(1, i+1):
        sum_var = sum_var + no

    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time/i
    return avg_time


def multiplication(i):

    start_time = time.time()

    mul_var = 1
    for no in range(1, i+1):
        mul_var = mul_var * no

    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time/i
    return avg_time


def division(i):

    start_time = time.time()

    div_var = 1
    for no in range(1, i+1):
        div_var = div_var / no

    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time/i
    return avg_time


if __name__ == "__main__":
    input_number = 10**6
    # addition_time = addition(input_number)
    # print(addition_time)  # 5.329394340515137e-08
    # multiplication_time = multiplication(input_number)
    # print(multiplication_time)  # 0.0005723469591140747
    division_time = division(input_number)
    print(division_time)  # 4.6875e-08
