from collections import defaultdict

class Tree:
    visited = []
    d=[]
    time = 0
    f=[]
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        pass
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

                    
    def dfs(self, v):
        self.visited[v] = 1
        self.d[v] = self.time
        self.time += 1
        for i in range(len(self.graph[v])):
            neighbour = self.graph[v][i]
            if not self.visited[neighbour]:
                self.dfs(neighbour)
        self.f[v] =  self.time
        self.time += 1
    
    def isParent(self,u,v):
        return self.d[u] < self.d[v] and self.f[v] < self.f[u]
    
            
    def solve(self):
        with open('ancestor.in', "r") as f:
            n = int(f.readline()) 
            self.visited = [0]*(n+1)
            self.d = [0]*(n+1)
            self.f = [0]*(n+1)
            parents = [int(x) for x in f.readline().split()] 
            for i in range(len(parents)):
                parent = parents[i]
                if not parent:
                    self.root = i+1
                else:
                    self.add_edge(parent,i+1)
            self.dfs(self.root)
            m = int(f.readline()) 
            with open('ancestor.out', "w") as fout:
                for i in range(m):
                    a,b = map(int, f.readline().split())
                    fout.write(str(+self.isParent(a,b)) + "\n")
        

tree = Tree()
tree.solve()