def fizzbuzz(n):
    """
    Prints the numbers from 1 to n with FizzBuzz replacements.

    Args:
        n: An integer.
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage:
n = 15
fizzbuzz(n)

n = 30
fizzbuzz(n)