def divide_numbers(a, b):
    """
    Divide two numbers.

    Parameters
  
    a : float
        The dividend
    b : float
        The divisor

    Returns
   
    float
        The quotient of the division
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
print(divide_numbers(3,6))
