# Fibonacci Sequence - 0 1 1 2 3 5 8 13 21 34 55 89 144 . . . .
def fibonacci(index):
    # if 'stop' conditions
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fibonacci(index - 1) + fibonacci(index - 2)  # Every term in fib sequence = sum of previous two terms

#                                 fib(4)
#              fib(3)=2              +                 fib(2)=1
#       fib(2)=1   +   fib(1)=1                 fib(1)=1  +  fib(0)=0
# fib(1)=1 + fib(0)=0
# Fibonacci recursion method sets up a tree, goes down it and then goes up

# Input is indexes
fibonacciSequence = []
for i in range(20):
    fibonacciSequence.append(fibonacci(i))
print(f"Fibonacci sequence => {fibonacciSequence}")
