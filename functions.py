import math

# 1. Simple Quadratic Function
def quadratic(x):
    """
    f(x) = x^2
    Global minimum at x = 0
    """
    return x ** 2


# 2. Cubic Polynomial Function
def cubic(x):
    """
    f(x) = x^3 - 6x^2 + 4x + 12
    Has multiple local minima
    """
    return x**3 - 6*x**2 + 4*x + 12


# 3. Trigonometric Function
def trigonometric(x):
    """
    f(x) = sin(x) + x^2
    Non-linear, multi-modal
    """
    return math.sin(x) + x**2


# Dictionary to access functions easily from GUI
FUNCTIONS = {
    "Quadratic: x²": quadratic,
    "Cubic Polynomial": cubic,
    "Trigonometric: sin(x) + x²": trigonometric
}
