from collections import defaultdict
from copy import deepcopy
# import io
# import os
 
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class Tree:
    ans = []
    cycle_is_found = False
    start = []
    path = []
    visited = []
    graph = defaultdict(list)
    
    def __init__(self):
        with open("cycle2.in", "r") as f:
            n, m = map(int, f.readline().split())
            for _ in range(m):
                a,b = map(int, f.readline().split())
                self.add_edge(a,b)
            self.n = n
            self.visited = [0]*(n+1)
        print(self.graph)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def dfs(self, node):  #function for dfs 
        if(self.cycle_is_found):
            return
        self.visited[node] = 1
        self.path.append(node)
        parent = self.graph[node]
        for i in range(len(parent)):
            to = parent[i]
            if(self.visited[to] == 1):
                self.path.append(to)
                self.cycle_is_found = True
                return
            else:
                self.dfs(to)
                if self.cycle_is_found:
                    return
        self.visited[node] = 2
        self.path.pop()
    
    def solve(self):
        for i in range(self.n):
            if self.visited[i] == 0:
                self.dfs(i)
            if self.cycle_is_found:
                break
        with open('cycle2.out', 'w') as f:
            if self.cycle_is_found:
                last = self.path[-1]
                i = len(self.path) - 2
                while self.path[i] != last:
                    i -= 1
                f.write('YES\n')
                f.write(' '.join([str(x) for x in self.path[:-1]]))
            else:
                f.write('NO')
                
           
tree = Tree()
tree.solve()


