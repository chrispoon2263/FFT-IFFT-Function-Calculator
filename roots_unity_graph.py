import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def get_x_y(points):
    x_output = []
    y_output = []
    for i in points:
        x_output.append(round(i.real, 2))
        y_output.append(round(i.imag, 2))
    return x_output, y_output


def get_point_representation(x_output, y_output):
    return list(zip(x_output, y_output))

def create_roots_unity_graph(file_name, points):
    matplotlib.use('agg')
    # turn off plot
    plt.ioff()

    # convert to numpy arrays
    x, y = get_x_y(points)
    x_list = np.array(x)
    y_list = np.array(y)


    # plot figure and save plot
    fig, ax = plt.subplots()

    # create scatter and add to plot
    plt.scatter(x_list, y_list, s=100, color='red')


    # create and add circle to plot
    circle1 = plt.Circle((0, 0), 1, fill=False)
    ax.add_patch(circle1)

    # add grid
    ax.grid(True, which='both')

    # add x and y axis
    plt.axvline(0, color='black')
    plt.axhline(0, color='black')

    # save file and close
    plt.savefig(file_name)
    plt.close(fig)



def main():
    points = [(1+0j), (-0.7071067811865476-0.7071067811865475j), (6.123233995736766e-17+1j), (0.7071067811865475-0.7071067811865476j), (-1+0j), (0.7071067811865476+0.7071067811865475j), (-6.123233995736766e-17-1j), (-0.7071067811865475+0.7071067811865476j)]
    #print(get_x_y(points))
    create_roots_unity_graph("static/images/roots_unity_graph.png", points)


if __name__ == "__main__":
    main()
