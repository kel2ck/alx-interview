#!/usr/bin/python3
'''
Method that determines the number of minmum operations given n characters
'''


def minOperations(n):
    """
    Calculates the fewest number of operations needed to obtain 
                        exactly `n` 'H' characters in the file.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
             Returns 0 if `n` is not an integer.

    """

    # Check if `n` is not an integer
    if not isinstance(n, int):
        return 0

    operations = 0
    i = 2
    while (i <= n):
        # Check if `n` is divisible by `i`
        if not (n % i):
            # Reduce `n` by dividing it by `i`
            n = int(n / i)
            # Increase the count of operations by `i`
            operations += i
            # Set `i` back to 1 to start checking from the beginning
            i = 1
        i += 1
    return operations
