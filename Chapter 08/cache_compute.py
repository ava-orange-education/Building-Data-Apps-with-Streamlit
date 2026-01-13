from timeit import timeit

counter = 0
cache = {}


def fibonacci(n):
    if n in cache:
        return cache[n]

    global counter
    counter += 1

    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    cache[n] = result
    return result


print(f"Time taken: {timeit(lambda: fibonacci(35), number=1)}s")
print(f"Number of function calls: {counter}")
