from functools import cache
from timeit import timeit

counter = 0


@cache
def fibonacci(n):
    global counter
    counter += 1

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(f"Time taken: {timeit(lambda: fibonacci(35), number=1)}s")
print(f"Number of function calls: {counter}")
