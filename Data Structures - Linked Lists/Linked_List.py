class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        '''
        { self.data,
        self.nextNode =}=> next Node
        '''


class LinkedList:
    def __init__(self):
        # Linked lists have two separate pointers / arrows
        self.head = None  # Pointer / arrow to the first node | Initialized to point to nothing
        self.tail = self.head  # Pointer / arrow to the last node | Points back to the head
        self.length = 0

    def append(self, data):
        newNode = Node(data)  # Prepare a new Node for the list
        if self.head is None:  # If the head arrow is pointing to nothing
            self.head = newNode  # HEAD => newNode
            self.tail = self.head  # Tail arrow points to head | HEAD <= TAIL
            self.length = 1  # Let it be known that the linked list has 1 entry so far

        else:
            # BEFORE: TAIL => last node in LL {self.data, self.nextNode =}=> None
            self.tail.nextNode = newNode  # Add extension node to the last node
            # AFTER: TAIL => 2nd to last node in LL {self.data, self.nextNode =}=> newNode

            # BEFORE: TAIL => 2nd to last node in LL {self.data, self.nextNode =}=> newNode
            self.tail = newNode  # Order tail pointer arrow to point to the node that was just recently added
            # AFTER: TAIL => last node in LL {self.data, self.nextNode =}=> None
            self.length += 1  # Increased current LL node count by 1

    def prepend(self, data):
        newNode = Node(data)  # Prepare a new Node for the list
        if self.head is None:  # If the head arrow is pointing to nothing
            self.head = newNode  # HEAD => newNode
            self.tail = self.head  # Tail arrow points to head | HEAD <= TAIL
            self.length = 1  # Let it be known that the linked list has 1 entry so far
        else:
            # BEFORE: HEAD => first node in LL {self.data, self.nextNode =}=> 2nd Node
            newNode.nextNode = self.head  # The newNode points to the node on the receiving end of the HEAD arrow pointer
            # AFTER: newNode {self.data, self.nextNode =}=> HEAD => first node in LL

            # BEFORE: newNode {self.data, self.nextNode =}=> HEAD => first node in LL
            self.head = newNode  # HEAD arrow pointer points to the newNode
            # AFTER: HEAD => newNode becomes 1st node in LL {self.data, self.nextNode =}=> 2nd node in LL (formerly 1st node)
            self.length += 1  # Increased current LL node count by 1

    def printList(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            currentNode = self.head  # currentNode is marker that focuses on HEAD or first node in LL
            while currentNode is not None:  # While loop that goes through all nodes until it reaches a None node
                print(currentNode.data, end="=>")
                currentNode = currentNode.nextNode  # Marker goes to the next node in LL
        print("None")

    def insert(self, position, data):
        if position >= self.length:  # If you want to put new node outside the boundaries of the current LL
            if position > self.length:
                print("Position unavailable. Inserting at the end of the list")
            self.append(data)  # Use append function to add to end of list
        elif position == 0:  # If user want to add to beginning of LL
            self.prepend(data)  # Use prepend function to add to start of LL
        else:
            newNode = Node(data)
            currentNode = self.head  # currentNode is marker that focuses on HEAD or first node in LL
            for nodes in range(position - 1):  # For loop that goes to just before target position in LL
                currentNode = currentNode.nextNode  # currentNode marker travels along the chain of pointer arrows
            '''
            HEAD=>{A|=}=>{B|=}=======>{C|=}=>{D|=}=>None
                             ↘{E|=}=>↗
            '''
            # Once currentNode marker in between appropriate nodes
            newNode.nextNode = currentNode.nextNode  # newNode and currentNode pointers point to same target
            # Nodes B and E both point to C, currentNode is Node B, newNode is Node E
            currentNode.nextNode = newNode  # currentNode points to newNode
            # Node B pointer arrow goes from Node C to new Node E
            self.length += 1

    def remove(self, position):
        if self.head is None:
            print("Linked List is empty")
            return
        if position == 0:
            self.head = self.head.nextNode  # Have HEAD point to the Node after the very first one
            if self.head is None or self.head.nextNode is None:  # If HEAD points to nothing or the node after the first one points to nothing
                self.tail = self.head  # Have TAIL point to HEAD
            self.length -= 1  # Reduce length by 1
            return
        if position >= self.length:
            position = self.length - 1  # Make position the end of LL
        currentNode = self.head  # currentNode is marker that focuses on HEAD or first node in LL
        for i in range(position - 1):  # For loop that goes to just before target position in LL
            currentNode = currentNode.nextNode  # currentNode marker travels along the chain of pointer arrows
        currentNode.nextNode = currentNode.nextNode.nextNode
        # If currentNode is Node B and currentNode.nextNode is Node E, currentNode.nextNode.nextNode is Node C
        # If B is currentNode then currentNode.nextNode.nextNode is B's neighbors neighbor aka Node C
        '''
        HEAD=>{A|=}=>{B|=}X=>{E|=}X=>{C|=}=>{D|=}=>None
                         ↘=========>↗
        '''
        self.length -= 1
        if currentNode.nextNode is None:  # If nothing after currentNode
            self.tail = currentNode  # TAIL points to currentNode
        return

    def reverse(self):
        reversedLL = [None] * self.length  # Array to hold the reversed LL values
        marker = -1  # Array index starts at very end of array
        if self.head is None:
            print("Empty Linked List")
        else:
            currentNode = self.head  # currentNode is marker that focuses on HEAD or first node in LL
            while currentNode is not None:  # While loop that goes through all nodes until it reaches a None node
                reversedLL[marker] = currentNode.data  # Place LL data into array starting from the back end
                marker -= 1  # Move index to the left of array
                currentNode = currentNode.nextNode  # Marker goes to the next node in LL
        print(reversedLL)


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(2, 24)
ll.reverse()
ll.printList()
ll.remove(2)
ll.printList()
ll.reverse()
