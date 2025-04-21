# def power_and_add_with_loop(n, m, addition):
#     """
#     Computes n raised to the power of m using a for loop and adds a given number.
#
#     :param n: The base number.
#     :param m: The exponent.
#     :param addition: The number to add to the result of n^m.
#     :return: The computed result.
#     """
#     result = 1  # Start with 1 because anything to the power of 0 is 1
#     for _ in range(m):  # Loop m times
#         result *= n  # Multiply n each time
#     result += addition  # Add the additional number
#     return result
#
#
# # Example usage
# n = 2
# m = 3
# addition = 5
# print(f"The result of {n}^{m} + {addition} is: {power_and_add_with_loop(n, m, addition)}")


def factorial_func(n):

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Try it out!
n = 5
print(f"The factorial of {n} is: {factorial_func(n)}")
