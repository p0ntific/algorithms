from collections import defaultdict
from copy import deepcopy
import io
import os
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class Tree:
    depth = 0
    def __init__(self):
        self.graph = defaultdict(list)
        self.set_data()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    # def set_data(self):
    #     with open('ej.in', "r") as f:
    #         n, k = map(int, f.readline().split())
    #         for _ in range(n-1):
    #             a,b = map(int, f.readline().split())
    #             self.add_edge(a,b)
    #         self.k = k
    #         self.len = len(self.graph)
    #         self.graph_copy = deepcopy(self.graph)
    def set_data(self):
        n,k = map(int, input().split())
        for _ in range(n-1):
            a,b = map(int, input().split())
            self.add_edge(a,b)
        self.k = k
        self.len = len(self.graph)
        self.graph_copy = deepcopy(self.graph)
        
    def is_hedgehog(self):
        self.depth += 1
        # проверка 1-ежовости
        n = len(self.graph)
        leaves = len([node for node in self.graph if len(self.graph[node]) == 1])
        if leaves + 1 == n and leaves >= 3:
            return True
        return False
    
    def solve(self):
        graph = self.graph
        n = len(graph)
        leaves = [node for node in graph if len(graph[node]) == 1]
        while n > 2:
            if self.is_hedgehog():
                if self.depth == self.k:
                    return 'Yes'
                else:
                    return 'No'
            n -= len(leaves)
            new_leaves = []
            neighbours = set()
            neighbours_cnt = [0]*(self.len+1)
            for leaf in leaves:
                neighbour = graph[leaf].pop()
                neighbours_cnt[neighbour] += 1
                #neighbours_cnt[neighbour] += (self.graph_copy[leaf])
                neighbours.add(neighbour)
                graph[neighbour].remove(leaf)
                graph.pop(leaf)
                if(len(graph[neighbour]) == 1):
                    new_leaves.append(neighbour)
            for i in neighbours_cnt:
                if i > 0 and i < 3:
                    return 'No'
                # if len(self.graph_copy[neighbour])<=3:
                #     return 'No'
            leaves = new_leaves.copy()  
            
        return 'No'
            
    
                
                    
tree = Tree()
print(tree.solve())


