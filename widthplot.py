import numpy as np
import matplotlib.pyplot as plt

widths = np.array([
    [12, 12, 12, 12, 12],
    [36, 24, 36, 24, 36],
    [132, 96, 96, 132, 84],
    [504, 240, 458, 432, 372],
    [1932, 1620, 2328, 1656, 1584],
    [11196, 10500, 10824, 10368, 11796]
])

def main():
    average_widths = np.mean(widths, axis=1)
    k_values = np.arange(1, 7)

    plt.plot(k_values, average_widths)

    for i, (x, y) in enumerate(zip(k_values, average_widths)):
        plt.text(x, y, f'({x},{y:.2f})', fontsize=9, ha='right')

    plt.xlabel('Number of moves applied to puzzle')
    plt.ylabel('Average number of nodes expanded in last iteration')
    plt.title('Plot of k-moves vs Average Width at Solution for A*')
    plt.show()



if __name__ == "__main__":
    main()