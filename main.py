def greeting():
    print("Hi There")


def calculate_pi():
    """
    Calculate pi to the 5th decimal digit using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    This method converges much faster than simpler formulas.
    Returns pi accurate to at least 5 decimal places (3.14159).
    """
    def arctan(x, num_terms=50):
        """Calculate arctan(x) using Taylor series expansion."""
        result = 0
        x_squared = x * x
        x_power = x
        
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * x_power / (2 * n + 1)
            x_power *= x_squared
        
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(1/5) - arctan(1/239))
    
    return pi