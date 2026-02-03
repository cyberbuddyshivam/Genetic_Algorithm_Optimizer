# Helper function: Calculate sine using Taylor series
def sin(x):
    """
    Calculate sin(x) using Taylor series expansion
    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    """
    # Normalize x to [-π, π] range
    pi = 3.14159265358979323846
    x = x % (2 * pi)
    if x > pi:
        x -= 2 * pi
    
    # Taylor series calculation
    result = 0
    term = x
    for n in range(15):  # 15 terms for good accuracy
        result += term
        term *= -x * x / ((2 * n + 2) * (2 * n + 3))
    return result


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
    return sin(x) + x**2


# Dictionary to access functions easily from GUI
FUNCTIONS = {
    "Quadratic: x²": quadratic,
    "Cubic Polynomial": cubic,
    "Trigonometric: sin(x) + x²": trigonometric
}
