class Queue:
    def __init__(self):
        self.stack1 = []  # The Primary Stack BOTTOM/LAST => [#, #, #] <= TOP/FIRST
        self.stack2 = []  # The Secondary Stack

    def peek(self):
        if len(self.stack1) == 0:
            print("Queue Empty")
        else:
            # STACK1 [three, two, one]
            return self.stack1[len(self.stack1) - 1]

    def enqueue(self, data):
        # BEFORE
        # STACK1 [three, two, one]
        # STACK2 []
        for i in range(len(self.stack1)):
            item = self.stack1.pop()
            self.stack2.append(item)
        # AFTER
        # STACK1 []
        # STACK2 [one, two, three]

        self.stack1.append(data)  # Append 'four' to stack1

        # BEFORE
        # STACK1 [four]
        # STACK2 [one, two, three]
        for i in range(len(self.stack2)):
            item = self.stack2.pop()
            self.stack1.append(item)
        # AFTER
        # STACK1 [four, three, two, one]
        # STACK2 []

        return

    def dequeue(self):
        if len(self.stack1) == 0:
            print("Queue Empty")
            return
        else:
            # BEFORE
            # STACK1 [four, three, two, one]
            return self.stack1.pop()
            # AFTER
            # STACK1 [four, three, two]

    def printQueue(self):
        if len(self.stack1) == 0:
            print("Queue Empty")
            return
        print("START: ", end='')
        for i in range(len(self.stack1) - 1, 0, -1):  # 'i' goes from rightmost index to zeroth/leftmost index at a rate of -1 (one at a time)
            print(f"{self.stack1[i]} -> ", end='')
        print(self.stack1[0])
        return

myQueue = Queue()
myQueue.enqueue(2)
myQueue.enqueue(5)
myQueue.enqueue(0)
myQueue.printQueue()

myQueue.dequeue()
myQueue.printQueue()

print(myQueue.peek())
myQueue.enqueue(9)
myQueue.printQueue()

myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.printQueue()
