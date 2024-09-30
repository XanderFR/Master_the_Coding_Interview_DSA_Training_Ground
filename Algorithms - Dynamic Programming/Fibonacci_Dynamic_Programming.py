from functools import lru_cache

calculations = 0  # Global variable for keeping track of the number of calculations each function takes


def fibonacci(number):
    global calculations
    calculations += 1
    if number < 2:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(f"Fibonacci => {fibonacci(30)}")
print(f"Fibonacci Calculations=> {calculations}")


cache = {}
calculations = 0


def fibonacciCache(number):
    global calculations
    calculations += 1
    if number in cache:  # Use previous calculations to speed up current calculations
        return cache[number]
    elif number < 2:
        return number
    else:
        cache[number] = fibonacciCache(number - 1) + fibonacciCache(number - 2)  # Add new fibonacci number to cache
        return cache[number]

print(f"FibonacciCache => {fibonacciCache(30)}")
print(f"FibonacciCache Calculations=> {calculations}")


calculations = 0


@lru_cache(maxsize=1000)
def fibonacciLRUCache(number):
    global calculations
    calculations += 1
    if number < 2:
        return number
    else:
        return fibonacciLRUCache(number - 1) + fibonacciLRUCache(number - 2)

print(f"FibonacciLRUCache => {fibonacciLRUCache(30)}")
print(f"FibonacciLRUCache Calculations=> {calculations}")
print(fibonacciLRUCache.cache_info())
