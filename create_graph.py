import matplotlib.pyplot as plt
import numpy as np
import matplotlib


# Returns a polynomial for x values for the coefs provided.
# coefficients must be in ascending order (x**0 to x**n).
def poly_coefficients(x, coeffs):
    y = 0
    for i in range(len(coeffs)):
        y += coeffs[i]*x**i
    return y


# Saves the graph to files
def save_graph(file_name, coeffs):
    matplotlib.use('agg')
    # turn off plot
    plt.ioff()

    # create x-values
    x = np.linspace(-20, 20, 50)

    # calculate the y value for each element of the x vector
    y = poly_coefficients(x, coeffs)

    # plot figure and save plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid(True, which='both')
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.savefig(file_name)
    plt.close(fig)


def main():
    save_graph("static/images/graph_1.png", [1, 0, 2, 3])


if __name__ == "__main__":
    main()
