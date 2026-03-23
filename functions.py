pi = 3.14159265358979323846


def sin(x):
    two_pi = 2 * pi
    x = x % two_pi
    if x > pi:
        x -= two_pi
    elif x < -pi:
        x += two_pi

    result = 0
    term = x
    for n in range(15):
        result += term
        term *= -x * x / ((2 * n + 2) * (2 * n + 3))
    return result


def cos(x):
    return sin(x + pi / 2)


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


def gradient_rastrigin(x):
    return [2 * xi + 20 * pi * sin(2 * pi * xi) for xi in x]


def gradient_descent(x0, iterations=10000, learning_rate=0.001, bounds=(-5.12, 5.12)):
    x = list(x0)
    lower, upper = bounds
    history = []

    for _ in range(iterations):
        grad = gradient_rastrigin(x)
        x = [max(lower, min(upper, xi - learning_rate * gi)) for xi, gi in zip(x, grad)]
        history.append(rastrigin(x))

    return history[-1], x, history


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
        "has_gradient": True,
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
