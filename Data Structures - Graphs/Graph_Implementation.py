# Adjacent List uses array indexes to represent numbered nodes in a graph
class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacencyList = {}  # We will use a dictionary vertex : [connections] | circled number : lines to other circled numbers

    def insertNode(self, data):
        # {data: []}
        if data not in self.adjacencyList:
            self.adjacencyList[data] = []  # To store the circled number's connections
            self.numberOfNodes += 1
            return

    def insertConnection(self, point1, point2):
        # Example
        # {1: [2, 3],
        # 2: [1, 3],
        # 3: [1, 2]}
        # point1: [point2]
        # point2: [point1]
        if point2 not in self.adjacencyList[point1]:  # If point1 is not connected to point2 | If point2 is not in point1's list
            # Register point1----point2
            self.adjacencyList[point1].append(point2)
            # Register point2----point1
            self.adjacencyList[point2].append(point1)
            return
        return "Edge already exists"

    def showConnections(self):
        for node in self.adjacencyList:
            # Turn every node into a string and unite them with spaces in-between
            print(f"{node} --> {' '.join(map(str, self.adjacencyList[node]))}")


myGraph = Graph()
myGraph.insertNode(1)
myGraph.insertNode(2)
myGraph.insertNode(3)
myGraph.insertNode(4)
myGraph.insertConnection(1, 2)
myGraph.insertConnection(1, 3)
myGraph.insertConnection(2, 3)
myGraph.insertConnection(4, 1)
myGraph.showConnections()
