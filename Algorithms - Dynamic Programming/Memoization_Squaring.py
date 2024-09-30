import random
from functools import lru_cache


array = [random.randint(1, 10) for number in range(50)]  # Prepare an array of 50 integers each somewhere between 1 and 10


def squaringWithoutMemoization(number):
    return number ** 2

squaringWithoutMemoizationArray = []
for index in range(len(array)):
    squaringWithoutMemoizationArray.append(squaringWithoutMemoization(array[index]))
print(f"squaringWithoutMemoizationArray => {squaringWithoutMemoizationArray}")


cache = {}  # Dictionary to hold a number and its square product


def squaringWithMemoization(number):
    if number in cache:  # If number and square product already in dictionary
        return cache[number]  # Use it / return it
    else:
        cache[number] = number**2  # Add new number: square product to dictionary
        return cache[number]

squaringWithMemoizationArray = []
for index in range(len(array)):
    squaringWithMemoizationArray.append(squaringWithMemoization(array[index]))
print(f"squaringWithMemoizationArray => {squaringWithMemoizationArray}")


@lru_cache(maxsize=1000)  # A cache similar to the one from the previous function | A cache bound to the function that stores and returns previous encountered elements and their square products
def squaring(number):
    return number**2

squaringArray = []
for index in range(len(array)):
    squaringArray.append(squaring(array[index]))
print(f"squaringArray => {squaringArray}")

print(f"Cache => {cache}")
print(f"squaringCacheInfo => {squaring.cache_info()}")
