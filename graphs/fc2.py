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
        stack.append(v)
        for neighbor in self.neighbours[v]:
            if not self.visited[neighbor]:
                self.dfs(neighbor, stack)

    def reversed(self, v, component):
        self.visited[v] = True
        component.add(v)
        for neighbor in self.rev_neighbours[v]:
            if not self.visited[neighbor]:
                self.reversed(neighbor, component)


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
                self.graph.reversed(v, component)
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

fc = FireCrackers()
fc.solve('firesafe.in', 'firesafe.out')
