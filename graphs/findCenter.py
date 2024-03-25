# Python3 implementation of the above approach

# To create tree
tree = {}
path = []
maxHeight, maxHeightNode = -1, -1

# Function to store the path
# from given vertex to the target
# vertex in a vector path
def getDiameterPath(vertex, targetVertex, parent, path):

	# If the target node is found,
	# push it into path vector
	if (vertex == targetVertex):
		path.append(vertex)
		return True

	for i in range(len(tree[vertex])):
		# To prevent visiting a
		# node already visited
		if (tree[vertex][i] == parent):
			continue

		# Recursive call to the neighbours
		# of current node inorder
		# to get the path
		if (getDiameterPath(tree[vertex][i], targetVertex, vertex, path)):
			path.append(vertex)
			return True
	return False

# Function to obtain and return the
# farthest node from a given vertex
def farthestNode(vertex, parent, height):
	global maxHeight, maxHeightNode
	# If the current height is maximum
	# so far, then save the current node
	if (height > maxHeight):
		maxHeight = height
		maxHeightNode = vertex

	# Iterate over all the neighbours
	# of current node
	if (vertex in tree):
		for i in range(len(tree[vertex])):
		
			# This is to prevent visiting
			# a already visited node
			if (tree[vertex][i] == parent):
				continue
				
			# Next call will be at 1 height
			# higher than our current height
			farthestNode(tree[vertex][i], vertex, height + 1)

# Function to add edges
def addedge(a, b):
	if (a not in tree):
		tree[a] = []

	tree[a].append(b)

	if (b not in tree):
		tree[b] = []

	tree[b].append(a)

def FindCenter(n):
	# Now we will find the 1st farthest
	# node from 0(any arbitrary node)

	# Perform DFS from 0 and update
	# the maxHeightNode to obtain
	# the farthest node from 0

	# Reset to -1
	maxHeight = -1

	# Reset to -1
	maxHeightNode = -1

	farthestNode(0, -1, 0)
class Graph:
    def __init__(self, n):
        self.n = n
        self.neighbours = [[] for _ in range(n + 1)]
        self.rev_neighbours = [[] for _ in range(n + 1)]
        self.visited = [False] * (n + 1)

    def add_edge(self, a, b):
        self.neighbours[a].append(b)
        self.rev_neighbours[b].append(a)

    def dfs(self, v, stack):
        self.visited[v] = True
        for neighbor in self.neighbours[v]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, stack)
        stack.append(v)

    def reversed_dfs(self, v, component):
        self.visited[v] = True
        component.add(v)
        for neighbor in self.rev_neighbours[v]:
            if not self.visited[neighbor]:
                self.reversed_dfs(neighbor, component)


class FireCrackers:
    def __init__(self):
        self.graph = None
        self.components = []
        self.fire_stations = set()
        self.v_sort = []

    def input_from_file(self, file):
        with open(file, 'r') as f:
            n = int(f.readline())
            m = int(f.readline())
            self.graph = Graph(n)

            for _ in range(m):
                a, b = map(int, f.readline().split())
                self.graph.add_edge(a, b)

    def find_fire_stations(self):
        for i in range(1, self.graph.n + 1):
            if not self.graph.visited[i]:
                self.graph.dfs(i, self.v_sort)

        self.graph.visited = [False] * (self.graph.n + 1)

        while self.v_sort:
            v = self.v_sort.pop()
            if not self.graph.visited[v]:
                component = set()
                self.graph.reversed_dfs(v, component)
                self.components.append(component)

        for component in self.components:
            edges = any(neighbor not in component for v in component for neighbor in self.graph.neighbours[v])

            if not edges:
                self.fire_stations.add(next(iter(component)))

    def print_answer_to_file(self, file):
        with open(file, 'w') as f:
            f.write(f"{len(self.fire_stations)}\n")
            f.write(" ".join(map(str, self.fire_stations)))

    def solve(self, input_file, output_file):
        self.input_from_file(input_file)
        self.find_fire_stations()
        self.print_answer_to_file(output_file)

# Usage
fc = FireCrackers()
fc.solve('firesafe.in', 'firesafe.out')

	# Stores one end of the diameter
	leaf1 = maxHeightNode

	# Similarly the other end of
	# the diameter

	# Reset the maxHeight
	maxHeight = -1
	farthestNode(maxHeightNode, -1, 0)

	# Stores the second end
	# of the diameter
	leaf2 = maxHeightNode

	# Store the diameter into
	# the vector path
	path = []

	# Diameter is equal to the
	# path between the two farthest
	# nodes leaf1 and leaf2
	getDiameterPath(leaf1, leaf2, -1, path)

	pathSize = len(path)

	if (pathSize % 2 == 1):
		print(path[int(pathSize / 2)]*-1)
	else:
		print(path[int(pathSize / 2)], ", ", path[int((pathSize - 1) / 2)], sep = "", end = "")

N = 13

tree = {}


addedge(1, 4)
addedge(2, 4)
addedge(3, 4)
addedge(4, 13)
addedge(10, 5)
addedge(11, 5)
addedge(12, 5)
addedge(14, 5)
addedge(5, 13)
addedge(6, 7)
addedge(8, 6)
addedge(13, 6)
addedge(9, 6)

FindCenter(N)

# This code is contributed by suresh07.
