import queue

with open('rootdist.in') as f:
    n = int(f.readline())
    graph = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        u = int(f.readline())
        graph[u].append(i)

nodes = []
stack = queue.Queue()
stack.put(1)#корень в 1
depth = -1
while not stack.empty():
    m = stack.qsize()
    depth += 1
    nodes.clear()
    for i in range(m):
        u = stack.get()
        nodes.append(u)
        for v in graph[u]:
            stack.put(v)

nodes.sort()
with open('rootdist.out','w') as f:
    f.write(str(depth) + '\n')
    f.write(str(len(nodes)) + '\n')
    for u in nodes:
        f.write(str(u)+" ")

