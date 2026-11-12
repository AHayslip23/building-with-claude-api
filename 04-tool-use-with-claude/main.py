def greeting():
    print("Hello, world!")


def calculate_pi_to_fifth_digit():
    """
    Calculate pi rounded to the fifth decimal digit (5 decimal places).
    Uses the Chudnovsky algorithm, which converges extremely quickly.

    The Chudnovsky formula:
        1/pi = (1 / 426880*sqrt(10005)) * SUM [ (6k)! * (13591409 + 545140134*k) ]
                                                   / [ (3k)! * (k!)^3 * (-262537412640768000)^k ]

    Each term of the series adds roughly 14-15 correct digits of pi, so only
    a small number of iterations are needed.

    Returns:
        float: The value of pi rounded to 5 decimal places (3.14159)
    """
    from decimal import Decimal, getcontext

    # Set precision high enough to guarantee 5 accurate decimal places
    getcontext().prec = 20

    def factorial(n):
        """Iterative factorial to avoid recursion limits."""
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)          # (6k)! / ((3k)! * (k!)^3)
    X = Decimal(1)          # (-262537412640768000)^k
    L = Decimal(13591409)   # 13591409 + 545140134*k
    K = Decimal(6)          # 6k term tracker

    total = L               # Summation accumulator (starts at k=0 term)

    # A handful of iterations is far more than enough for 5 decimal places
    num_iterations = 5
    for k in range(1, num_iterations + 1):
        # Update multiplier M using the ratio between consecutive terms
        M = M * Decimal(factorial(6 * k)) / (
            Decimal(factorial(3 * k)) * Decimal(factorial(k)) ** 3
        )
        X *= Decimal(-262537412640768000)
        L += Decimal(545140134)
        total += M * L / X

    pi = C / total
    return float(round(pi, 5))


def calculate_pi(precision=5):
    """
    Calculate pi to a specified number of decimal places.
    Uses the Leibniz formula: pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
    
    Args:
        precision: Number of decimal places to calculate (default: 5)
    
    Returns:
        float: Approximation of pi
    """
    pi_approx = 0.0
    iterations = 10000000  # Higher iterations for better accuracy
    
    for i in range(iterations):
        term = ((-1) ** i) / (2 * i + 1)
        pi_approx += term
    
    pi_approx *= 4
    
    # Round to specified precision
    return round(pi_approx, precision)


def calculate_pi_machin():
    """
    Calculate pi using Machin's formula for faster convergence.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    Uses Taylor series for arctan.
    
    Returns:
        float: Approximation of pi to 5 decimal places
    """
    def arctan(x, terms=100):
        """Calculate arctan using Taylor series"""
        result = 0.0
        x_squared = x * x
        x_power = x
        
        for n in range(terms):
            sign = (-1) ** n
            result += sign * x_power / (2 * n + 1)
            x_power *= x_squared
        
        return result
    
    pi_approx = 4 * (4 * arctan(1/5, 100) - arctan(1/239, 100))
    return round(pi_approx, 5)