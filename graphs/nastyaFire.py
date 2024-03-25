import sys
sys.setrecursionlimit(5000)

def DFS(v):
    visited[v] = True
    for neighbor in adjacency[v]:
        if not visited[neighbor]:
            DFS(neighbor)
    vertex_sort.append(v)

def DFS_reverse(v):
    visited[v] = True
    component.add(v)
    for neighbor in rev_adjacency[v]:
        if not visited[neighbor]:
            DFS_reverse(neighbor)
            
def find_fire_station():
    for component in components:
        edges = False

        for vertex in component:
            for neighbor in adjacency[vertex]:
                if neighbor not in component:
                    edges = True
                    break

            if edges:
                break

        if not edges:
            fire_stations.add(next(iter(component)))
    

with open('firesafe.in', 'r') as fin:
    n = int(fin.readline())
    m = int(fin.readline())

    adjacency = [[] for _ in range(n + 1)]
    rev_adjacency = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, fin.readline().split())
        adjacency[a].append(b)
        rev_adjacency[b].append(a)

    vertex_sort = []
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            DFS(i)

    visited = [False] * (n + 1)
    components = []

    while vertex_sort:
        v = vertex_sort.pop()
        if not visited[v]:
            component = set()
            DFS_reverse(v)
            components.append(component)

    fire_stations = set()

    find_fire_station()

with open('firesafe.out', 'w') as fout:
    fout.write(str(len(fire_stations)) + '\n')
    for station in fire_stations:
        fout.write(str(station) + " ")
