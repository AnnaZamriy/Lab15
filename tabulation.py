import numpy as np

def tabulate_function(x_min, x_max, num_points=50):
    x = np.linspace(x_min, x_max, num_points)
    y = x**2 + np.sin(x)
    return x, y
    