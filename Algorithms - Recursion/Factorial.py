def factorialLoop(number):
    product = 1  # The starting number
    for num in range(1, number + 1):  # Range goes from 1 to number
        product *= num
    return product


def factorialRecursive(number):
    if number <= 1:  # The stop condition
        return 1
    else:
        return number * factorialRecursive(number - 1)
    # Recursive chain goes number * fR(number-1) * fR(number-2) * ... * fR(1)

print(factorialLoop(50))
print(factorialRecursive(50))
