class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None  # Pointer arrow to the next node in the stack


class Stack:
    def __init__(self):
        """
        # <= TOP
        #
        # <= BOTTOM
        """
        self.top = None  # Pointer arrow to the top of stack
        self.bottom = None  # Pointer arrow to the bottom of stack
        self.length = 0

    def peek(self):
        if self.top is None:
            return None
        return self.top.data  # Return the data from the node TOP is pointing to

    def push(self, data):
        newNode = Node(data)
        if self.top is None:  # For empty stack
            self.top = newNode
            self.bottom = newNode
            """
            TOP => # <= BOTTOM
            """
        else:
            # BEFORE
            """
            #⬇ <= TOP
            # <= BOTTOM
            """
            newNode.nextNode = self.top
            # AFTER
            """
            #⬇ newNode.nextNode⬇ arrow points down to node receiving the TOP arrow
            #⬇ <= TOP
            # <= BOTTOM
            """

            # BEFORE
            """
            #⬇ newNode.nextNode⬇ arrow points down to node receiving the TOP arrow
            #⬇ <= TOP
            # <= BOTTOM
            """
            self.top = newNode  # TOP arrow points to newNode
            # AFTER
            """
            #⬇ newNode.nextNode <= TOP
            #⬇ 
            # <= BOTTOM
            """
        self.length += 1

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            # BEFORE
            """
            #⬇ <= TOP
            #⬇ 
            # <= BOTTOM
            """
            self.top = self.top.nextNode  # TOP points to the second-highest node in the stack
            # BEFORE
            """
            #⬇ 
            #⬇ <= TOP
            # <= BOTTOM
            """
            self.length -= 1
            if self.length == 0:
                self.bottom = None

    def printStack(self):
        if self.top is None:
            print("Stack empty")
        else:
            currentPointer = self.top  # Marker that starts on top of stack | Receiving node of TOP
            while currentPointer is not None:
                print(currentPointer.data)
                currentPointer = currentPointer.nextNode  # Travel along the currentNode's arrow to the next node

myStack = Stack()

print(myStack.peek)
print()

myStack.push('google')
myStack.push('udemy')
myStack.push('discord')

print(myStack.top.data)
print(myStack.bottom.data)
print()

myStack.pop()
myStack.printStack()
print()

myStack.pop()
myStack.pop()

myStack.printStack()
