import sys
sys.setrecursionlimit(5000)

class FireSafe:
    graph = []
    depth = 0
    max_depth = 0
    rev_graph = []
    visited =[]
    bad_points = []
    component = set()
    components = []
    def __init__(self) -> None:
        with open('firesafe.in') as f:
            n = int(f.readline())
            m = int(f.readline())
            self.n = n
            self.m = m
            self.graph = [[] for _ in range(n+1)]
            self.rev_graph = [[] for _ in range(n+1)]
            self.visited = [False for _ in range(n+1)]
            for _ in range(m):
                u,v = map(int, f.readline().split())
                self.add_edge(u,v)
                
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.rev_graph[v].append(u)
    
    def dfs_front(self,v):
        self.visited[v] = True
        for neighbour in self.graph[v]:
            if not self.visited[neighbour]:
                self.dfs_front(neighbour)
        self.bad_points.append(v)
        
    def dfs_back(self,v):
        self.visited[v] = True
        self.component.add(v)
        for neighbour in self.rev_graph[v]:
            if not self.visited[neighbour]:
                self.dfs_back(neighbour)
        
    
    def find_station(self):
        ans = set()
        for block in self.components:
            is_good = False
            for v in block:
                # set неперебираем
                # надо рассматривать не graph[i] а graph[block[i]]
                for neighbour in self.graph[v]:
                    if neighbour not in block:
                        is_good = True
                        break
                    
                if is_good:
                    break
            if not is_good:
                ans.add(next(iter(block)))    
        return ans          
    
    def solve(self):
        
        for i in range(1, self.n+1):
            if not self.visited[i]:
                self.dfs_front(i)
        self.visited = [False]*(self.n+1)
        #print(self.bad_points)
        while self.bad_points:
            #
            point = self.bad_points.pop()
            if not self.visited[point]:
                self.dfs_back(point)
                
                self.components.append(self.component)
                # обновляем компоненту
                self.component = set()
        
        ans = self.find_station()
        with open('firesafe.out','w') as f:
            f.write(str(len(ans)) + '\n')
            f.write(" ".join([str(x) for x in ans]))

fs = FireSafe()
fs.solve()