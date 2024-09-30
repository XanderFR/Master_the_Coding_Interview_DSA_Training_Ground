class Node:
    """
        (data)
       🡧     🡦
    """
    def __init__(self, data):
        self.data = data
        self.leftNode = None  # The arrow pointing downward left
        self.rightNode = None  # The arrow pointing downward right


class BinarySearchTree:
    def __init__(self):
        self.root = None  # ROOT starts off as nothing, but it will have an arrow pointing to the first BST node
        '''
        ROOT
         🡣
        None
        '''
        self.numberOfNodes = 0

    def insert(self, data):
        print(f"Inserting {data}")
        newNode = Node(data)
        if self.root is None:
            self.root = newNode  # Set ROOT to point its arrow to newNode
            '''
            ROOT
             🡣
            (newNode)
            '''
            self.numberOfNodes += 1
        else:
            currentNode = self.root  # Set a node-shaped marker to point to / highlight ROOT
            # While loop breaking conditions
            '''LEFT
                (data)
               🡧     
            newNode
            '''
            '''RIGHT
                (data)
                     🡦
                    newNode
            '''
            while (currentNode.leftNode != newNode) and (currentNode.rightNode != newNode):  # While loop that runs as long and the node-shaped marker's left or right arrow is not connected to newNode
                # Right path
                if newNode.data > currentNode.data:
                    if currentNode.rightNode is None:  # If the node-shaped marker's right arrow points to nothing
                        currentNode.rightNode = newNode  # Set right arrow to point to newNode
                    else:  # If the right arrow is connected to another Node
                        currentNode = currentNode.rightNode  # Have the node-shaped marker travel down its right arrow to the next node
                        # Restart the cycle
                # Left path
                elif newNode.data < currentNode.data:
                    if currentNode.leftNode is None:  # If the node-shaped marker's left arrow points to nothing
                        currentNode.leftNode = newNode  # Set left arrow to point to newNode
                    else:  # If the left arrow is connected to another Node
                        currentNode = currentNode.leftNode  # Have the node-shaped marker travel down its left arrow to the next node
                        # Restart the cycle
            self.numberOfNodes += 1
            return

    def search(self, target):
        print(f"Searching for {target}: ", end='')
        if self.root is None:
            return "Tree Is Empty"
        else:
            currentNode = self.root  # Have the currentNode node-shaped marker point to ROOT
            while True:
                if currentNode is None:  # If currentNode goes down the tree all the way to a None node
                    return "Not Found"
                if currentNode.data == target:  # Target Found
                    return "Found"
                elif currentNode.data > target:  # If target is smaller than currentNode's data number
                    currentNode = currentNode.leftNode  # Marker travels down its left arrow
                elif currentNode.data < target:  # If target is larger than currentNode's data number
                    currentNode = currentNode.rightNode  # Marker travels down its right arrow

    def remove(self, target):
        print(f"Removing {target}")
        if self.root is None:
            return "Tree Is Empty"
        # It takes two node-shaped markers to delete a target node | one to mark the doomed node and another to replace
        currentNode = self.root  # Prepare a node-shaped marker attached to ROOT node
        parentNode = None  # A partner node-shaped marker to currentNode
        # While traversing the tree, parentNode stays with the doomed one while currentNode moves on to nodes lower on the tree to find a replacement
        while currentNode is not None:  # While currentNode points to something
            if currentNode.data > target:
                parentNode = currentNode  # parentNode stays with currentNode's target
                currentNode = currentNode.leftNode  # currentNode moves down its left arrow
            elif currentNode.data < target:
                parentNode = currentNode  # parentNode stays with currentNode's target
                currentNode = currentNode.rightNode  # currentNode moves down its right arrow
            else:  # Target found | currentNode.data == target
                # Doomed node has left child only
                '''LEFT
                    (target)
                   🡧       🡦
                {child}     None
                '''
                # Doomed node has right child only
                '''RIGHT
                    (target)
                   🡧       🡦
                None        {child}
                '''
                # Doomed node connected to nothing
                '''NEITHER
                    (target)
                   🡧       🡦
                None        None
                '''
                # Doomed node has two children
                '''BOTH
                    (target)
                   🡧       🡦
                {child}     {child}
                '''

                # Doomed node has left child only
                if currentNode.rightNode is None:
                    if parentNode is None:  # If parentNode target is the one going away
                        self.root = currentNode.leftNode  # Bring left node up to take its place
                        return
                    else:
                        if parentNode.data > currentNode.data:
                            parentNode.leftNode = currentNode.leftNode  # Connect parentNode's left arrow to whatever currentNode's left arrow is pointing to
                            return
                        else:
                            parentNode.rightNode = currentNode.leftNode  # Connect parentNode's right arrow to whatever currentNode's left arrow is pointing to
                            return

                # Doomed node has right child only
                elif currentNode.leftNode is None:
                    if parentNode is None:  # If parentNode target is the one going away
                        self.root = currentNode.rightNode  # Bring right node up to take its place
                        return
                    else:
                        if parentNode.data > currentNode.data:
                            parentNode.leftNode = currentNode.rightNode  # Connect parentNode's left arrow to whatever currentNode's right arrow is pointing to
                            return
                        else:  # parentNode.data < currentNode.data
                            parentNode.rightNode = currentNode.rightNode  # Connect parentNode's right arrow to whatever currentNode's right arrow is pointing to
                            return

                # Doomed node connected to nothing
                elif currentNode.leftNode is None and currentNode.rightNode is None:
                    if parentNode is None:  # Node to be deleted is ROOT
                        currentNode = None
                        return
                    if parentNode.data > currentNode.data:
                        parentNode.leftNode = None  # parentNode left arrow points to nothing
                        return
                    else:  # parentNode.data < currentNode.data
                        parentNode.rightNode = None  # parentNode right arrow points to nothing
                        return

                # Doomed node has two children
                elif currentNode.leftNode is not None and currentNode.rightNode is not None:
                    # Create two node-shaped markers attached to the target Node's right arrow receiver
                    # From the start, currentNode is equal to target node | The node to be removed
                    '''
                    (target|currentNode)
                               🡦
                            {delNode|currentNode.rightNode|delNodeParent}
                    '''
                    # delNode means node to be deleted, the node to be removed from the bottom of the tree to replace the target
                    delNode = currentNode.rightNode
                    delNodeParent = currentNode.rightNode
                    while delNode.leftNode is not None:  # While the current delNode's left arrow points to a non-None node
                        # Check if delNode's left arrow points to a valid node
                        # Loop to reach the leftmost node of the right subtree of the current node
                        # From delNode, travel left until you reach a childless Node

                        delNodeParent = delNode  # delNodeParent holds delNode's original position on the tree
                        delNode = delNode.leftNode  # delNode goes down its left arrow
                        # delNodeParent follows delNode from behind like a caterpillar
                    # Once delNode is on a tree node without children at the very bottom of the tree
                    currentNode.data = delNode.data  # Set the target node's (currentNode) data value to match delNode's
                    if delNode == delNodeParent:  # If the node to be deleted is the exact right child of currentNode
                        currentNode.rightNode = delNode.rightNode  # Connect currentNode's right arrow to the target of delNode's right arrow
                        return
                    if delNode.rightNode is None:  # If the leftmost node of the right subtree of the current node has no right subtree
                        delNodeParent.leftNode = None  # delNodeParent's left arrow points to None
                        return
                    else:  # If it has a right subtree, we simply link it to the parent of the del_node
                        delNodeParent.leftNode = delNode.rightNode  # connect delNodeParent's left arrow to the target of delNode's right arrow
                        return
        return "Not Found"

    def breadthFirstSearch(self):
        # Example tree
        """
                  {9}
               🡧      🡦
            {4}         {20}
          🡧   🡦        🡧   🡦
        {1}   {6}   {15}    {170}
        """
        currentNode = self.root  # Start BFS at ROOT | ROOT = 9
        if currentNode is None:  # Empty tree
            return "Tree is empty"
        else:
            BFSResult = []  # To store numbers in order of breadth first search | Left to right number nodes
            queue = []  # To keep track of the children of each node | Helps to ensure we go left to right

            queue.append(currentNode)  # Add ROOT to queue first | queue = [9]

            while len(queue) > 0:  # While the list of child nodes has stuff  in it
                currentNode = queue.pop(0)  # We extract the first element of queue and make it currentNode | currentNode = 9 | queue = []
                BFSResult.append(currentNode.data)  # Push currentNode data to BFSResult list as we are currently on the currentNode | BFSResult = [9]

                if currentNode.leftNode:  # If currentNode has left child, append to the queue | currentNode.leftNode = 4
                    queue.append(currentNode.leftNode)  # queue = [4]
                if currentNode.rightNode:  # If currentNode has right child, append to the queue | currentNode.rightNode = 20
                    queue.append(currentNode.rightNode)  # queue = [4 ,20]
                # And the cycle repeats, this time with 4
            return BFSResult  # Return the BFS array

    def RecursiveBFS(self, queue, BFSList):
        # queue = to keep track of the children of each node
        # BFSList = to store numbers in order of breadth first search
        if self.root is None:
            return "Tree is empty"
        if len(queue) == 0:
            return BFSList
        currentNode = queue.pop(0)  # We extract the first element of queue and make it currentNode
        BFSList.append(currentNode.data)  # Push currentNode data to BFSResult list as we are currently on the currentNode
        if currentNode.leftNode:
            queue.append(currentNode.leftNode)
        if currentNode.rightNode:
            queue.append(currentNode.rightNode)
        return self.RecursiveBFS(queue, BFSList)

bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
print(f"Breadth First Search => {bst.breadthFirstSearch()}")

