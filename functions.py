from math import cos, pi


def sin(x):
    result = 0
    term = x
    for n in range(15):
        result += term
        term *= -x * x / ((2 * n + 2) * (2 * n + 3))
    return result


def quadratic(x):
    return x[0] ** 2


def cubic(x):
    return x[0] ** 3 - 6 * x[0] ** 2 + 4 * x[0] + 12


def trigonometric(x):
    return sin(x[0]) + x[0] ** 2


def sphere(x):
    return sum(xi**2 for xi in x)


def rastrigin(x):
    return 10 * len(x) + sum(xi**2 - 10 * cos(2 * pi * xi) for xi in x)


def rosenbrock(x):
    return sum(
        100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2 for i in range(len(x) - 1)
    )


FUNCTION_INFO = {
    "Quadratic: x²": {
        "function": quadratic,
        "min_dimensions": 1,
        "max_dimensions": 1,
        "bounds": (-10, 10),
        "optimum_value": 0,
        "optimum_desc": "x = 0",
    },
    "Cubic Polynomial": {
        "function": cubic,
        "min_dimensions": 1,
        "max_dimensions": 1,
        "bounds": (-10, 10),
        "optimum_value": None,
        "optimum_desc": None,
    },
    "Trigonometric: sin(x) + x²": {
        "function": trigonometric,
        "min_dimensions": 1,
        "max_dimensions": 1,
        "bounds": (-10, 10),
        "optimum_value": None,
        "optimum_desc": None,
    },
    "Sphere": {
        "function": sphere,
        "min_dimensions": 2,
        "max_dimensions": 20,
        "bounds": (-5.12, 5.12),
        "optimum_value": 0,
        "optimum_desc": "origin (all zeros)",
    },
    "Rastrigin": {
        "function": rastrigin,
        "min_dimensions": 2,
        "max_dimensions": 20,
        "bounds": (-5.12, 5.12),
        "optimum_value": 0,
        "optimum_desc": "origin (all zeros)",
    },
    "Rosenbrock": {
        "function": rosenbrock,
        "min_dimensions": 2,
        "max_dimensions": 20,
        "bounds": (-2.048, 2.048),
        "optimum_value": 0,
        "optimum_desc": "all ones",
    },
}
