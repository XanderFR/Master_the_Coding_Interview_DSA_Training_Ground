class Stack:
    def __init__(self):
        self.array = []  # The stack

    def peek(self):
        return self.array[len(self.array) - 1]  # Return the rightmost data from array

    def push(self, data):
        self.array.append(data)
        return

    def pop(self):
        if len(self.array) != 0:  # If length of self.array is NOT equal to 0
            self.array.pop()
            return
        else:
            print("Stack Empty")
            return

    def printStack(self):
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])
        return

myStack = Stack()
myStack.push("Andrei's")
myStack.push("Courses")
myStack.push("Are")
myStack.push("Awesome")
myStack.printStack()
print()

myStack.pop()
myStack.pop()
myStack.printStack()
print()

print(myStack.peek())
