class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None  # nextNode start off as None | nextNode points rightwards =>


"""
{one}=> {two}=> {three}
⬆first           last⬆
"""


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        """
        {none}=> {none}
        ⬆first   last⬆
        """
        self.length = 0

    def peek(self):
        """
        {one}=> {two}=> {three}
        ⬆first           last⬆
        """
        return self.first.data  # Return data from the front of the line

    def enqueue(self, data):  # Enter the line
        newNode = Node(data)
        if self.last is None:  # Empty queue
            self.last = newNode
            self.first = self.last
            """
                 {one}
            first⬆   ⬆last
            """
            self.length += 1
        else:
            # BEFORE
            """
            {one}=> {two}           {three}
            ⬆first  last⬆
            """
            self.last.nextNode = newNode  # The last node's right arrow points to newNode
            # AFTER
            """
            {one}=> {two}====> three}
            ⬆first  last⬆
            """

            # BEFORE
            """
            {one}=> {two}====> {three}
            ⬆first  last⬆
            """
            self.last = newNode  # LAST points to recently added node
            # AFTER
            """
            {one}=> {two}=> {three}
            ⬆first           last⬆
            """

            self.length += 1

    def dequeue(self):  # Exit the line
        if self.last is None:
            print("Queue Empty")
            return
        if self.last == self.first:  # FIRST and LAST point to same single node
            """
                 {one}
            first⬆   ⬆last
            """
            self.last = None  # Set LAST to pont to nothing

        # BEFORE
        """
        {one}=> {two}=> {three}
        ⬆first           last⬆
        """
        self.first = self.first.nextNode  # Set FIRST to point to the node after the one at the front of the line
        # AFTER
        """
        {one}=> {two}=> {three}
                 ⬆first  last⬆
        """
        # AFTER PART 2
        """
        {two}=> {three}
         ⬆first  last⬆
        """
        self.length -= 1

    def printQueue(self):
        if self.length == 0:
            print("Queue Empty")
        else:
            print("FIRST: ", end='')
            currentPointer = self.first  # Marker that starts at FIRST
            while currentPointer is not None:
                if currentPointer.nextNode is None:  # Only one node
                    print(currentPointer.data)
                else:
                    print(f"{currentPointer.data}->", end='')
                currentPointer = currentPointer.nextNode  # Travel along the node arrows
            return


myQueue = Queue()
myQueue.enqueue("This")
myQueue.enqueue("is")
myQueue.enqueue("a")
myQueue.enqueue("Queue")
myQueue.printQueue()


print(myQueue.peek())


myQueue.dequeue()
myQueue.dequeue()
myQueue.printQueue()

myQueue.dequeue()
myQueue.dequeue()
myQueue.printQueue()
