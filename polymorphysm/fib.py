def fib(n):
    """
    Returns the fibonacci number in the Nth sequence
    Example F1 = 1, F2 = 1, F3 = 2
    fib(2): return: 1
    fib(3): return: 2
    """
    if n == 1:
        return 1

    elif n == 2:
        return 1

    else:
        return fib(n-1) + fib(n-2)


print(fib(25))
