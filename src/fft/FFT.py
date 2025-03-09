# Time complexity naive approach: O(n^2)
# Time complexity: O(nlog(n))
# https://www.youtube.com/watch?v=h7apO7q16V0
# https://en.wikipedia.org/wiki/DFT_matrix
# https://en.wikipedia.org/wiki/Fast_Fourier_transform

# Naive algorithm of multiplying polynomials is n^2
# Example: Multiply (1 + 2x + x^2 )(1 - 2x + x^2) = 1 -2x^2 + x^4
#                   [1, 2, 1]   *  [1, -2, 1] =     [1, 0, -2, 0, 1]
# Cooley-Tukey Implentation of FFT: requires power of 2 (pad inputs to be the next power of 2)

import matplotlib.pyplot as plt
import numpy as np
import math



def roots_of_unity(j, n):
    # Precondition: n must be greater than 1 and a power of 2
    # ex: 2, 4, 8, 16, 32 ... 2^n
    return math.e ** ((2 * math.pi * 1j * j) / n)


def roots_of_unity_IFFT(j, n):
    # Precondition: n must be greater than 1 and a power of 2
    # ex: 2, 4, 8, 16, 32 ... 2^n
    return math.e ** ((-2 * math.pi * 1j * j) / n)


def FFT(P):
    # Pre-condition: n must be a power of 2
    n = len(P)

    # base case
    if n == 1:
        return P

    # Recursive Case: Divide list into even/odd terms
    even, odd = P[::2], P[1::2]
    y_even, y_odd = FFT(even), FFT(odd)

    # Conquer Step: Combine
    y = [0] * n
    for j in range(n//2):
        w_j = roots_of_unity(j, n)
        y[j] = y_even[j] + w_j * y_odd[j]
        y[j + n//2] = y_even[j] - w_j * y_odd[j]
    return y


def IFFT(P):
    # need to divide DFT matrix ^-1  by n at the end
    n = len(P)
    y = IFFT_helper(P)
    return list(map(lambda x: x / n, y))


def IFFT_helper(P):
    # Pre-condition: n must be a power of 2
    n = len(P)

    # base case
    if n == 1:
        return P

    # Recursive Case: Divide list into even/odd terms
    even, odd = P[::2], P[1::2]
    y_even, y_odd = IFFT_helper(even), IFFT_helper(odd)

    # Conquer Step: Combine
    y = [0] * n
    for j in range(n // 2):
        w_j = roots_of_unity_IFFT(j, n)
        y[j] = (y_even[j] + w_j * y_odd[j])
        y[j + n // 2] = y_even[j] - w_j * y_odd[j]
    return y

# Pad lists to nearest power of 2
def pad_list(list_A, list_B):
    length = ((len(list_A) - 1) + (len(list_B) - 1)) + 1
    pad_length = 1

    # Find the next power of 2
    while pad_length < length:
        pad_length = pad_length * 2

    pad_A = [0] * pad_length
    pad_B = [0] * pad_length
    pad_C = [0] * pad_length
    pad_D = [0] * length

    # copy over values from list_A to pad_A
    for i in range(len(list_A)):
        pad_A[i] = list_A[i]

    # copy over values from list_B to pad_B
    for i in range(len(list_B)):
        pad_B[i] = list_B[i]

    return pad_A, pad_B, pad_C, pad_D


# Application of FFT/IFFT algorithm for polynomial multiplication
def multiply_polynomials(list_A, list_B, rounding):
    # Example: Multiply (1 + 2x + x^2 )(1 - 2x + x^2) = 1 -2x^2 + x^4
    #                   [1, 2, 1]   *  [1, -2, 1] =     [1, 0, -2, 0, 1]
    # Pad both polynomial representations to nearest power of 2 based on the final answer
    # A = [1, 2, 1]  # 1 + 2x + x^2 => [1, 2, 1, 0, 0, 0, 0, 0]
    # B = [1, -2, 1] # 1 - 2x + x^2 => [1, 2, 1, 0, 0, 0, 0, 0]
    # C =                           => [0, 0, 0, 0, 0, 0, 0, 0]
    # c1 =                          => [0, 0, 0, 0, 0] will be used for the final answer
    pad_A, pad_B, pad_C, c1 = pad_list(list_A, list_B) #O(n)

    # Convert to the point representation of the polynomial O(nlogn)
    a1 = FFT(pad_A)
    b1 = FFT(pad_B)


    # Multiply the point representation  O(n)
    for i in range(len(a1)):
        pad_C[i] = a1[i] * b1[i]

    # Convert back to the polynomial representation O(nlogn)
    C = IFFT(pad_C)

    # copy over values from C to c1 by unpadding the array
    for i in range(len(c1)):
        c1[i] = round(C[i].real, rounding) + round(C[i].imag, rounding) * 1j
    return a1, b1, pad_C, c1


def main():
    print(multiply_polynomials([1, 2, 1], [1, -2, 1], 10)[2])
    #print(multiply_polynomials([1, 2, 3], [2, 3, 4], 10))
    #print(multiply_polynomials([0, 0, 1], [0, 0, 0, 1], 10)[3])

if __name__ == "__main__":
    main()
