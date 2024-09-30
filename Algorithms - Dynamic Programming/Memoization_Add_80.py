from functools import lru_cache


def add_80(number):
    return number + 80

print(add_80(5))


cache = {}


def memoized_add_80(number):
    if number in cache:
        return number + 80
    else:
        cache[number] = number + 80
        return cache[number]

print(memoized_add_80(7))


@lru_cache(maxsize=1000)  # A cache similar to the one from the previous function | A cache bound to the function that stores and returns previously encountered elements and their sums
def memoized_add_80_II(number):
    return number + 80

print(memoized_add_80_II(8))

