import matplotlib.pyplot as plt
import numpy as np
from sympy import sympify, Poly, var
import re


# Converts String function to a list of numbers
def convert_to_list(string_input):
    # lower case the whole string, remove front and back white spaces
    output = string_input.strip().lower()

    # Use regex to add * between number and x
    output = re.sub(r"(\d)([a-z])", r"\1*\2", output)

    # devine a variable for sympy
    x = var("x")

    # Group like terms and reorder from smallest to largest and pad coefficients
    expr = Poly(sympify(output), x)
    coefs = expr.all_coeffs()
    coefs.reverse()

    x = list(map(int, coefs))
    return x



def main():
    #x = " X^2 +x"
    #x = "2x^2+ 7x^2 + 11x - 20 + 8x^3"
    x = "2x^2 + 2x^2"
    print(convert_to_list(x))
    

if __name__ == "__main__":
    main()
