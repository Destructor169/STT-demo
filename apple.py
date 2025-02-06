# simple_calculator.py

def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtracts the second number from the first.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The difference between a and b.
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divides the first number by the second.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float: The result of division.
    
    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b


def main():
    """
    Main function to run the calculator with example operations.
    """
    try:
        # Example operations
        num1 = 10
        num2 = 5

        print(f"Adding: {num1} + {num2} = {add(num1, num2)}")
        print(f"Subtracting: {num1} - {num2} = {subtract(num1, num2)}")
        print(f"Multiplying: {num1} * {num2} = {multiply(num1, num2)}")
        print(f"Dividing: {num1} / {num2} = {divide(num1, num2)}")

        # Example of an exception
        print(f"Dividing by zero: {divide(num1, 0)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

