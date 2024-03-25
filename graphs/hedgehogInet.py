from collections import defaultdict

n, k = map(int, input().split())
grafo = defaultdict(list)
degree = defaultdict(int)
p = defaultdict(int)
temp = []
band = True
h = 0
c = 0
d = 0
mayor = 0

def dfs(u):
    global h, band
    if h < k:
        if degree[u] < 3:
            band = False
    if h == k:
        if degree[u]:
            band = False
    h += 1
    for v in grafo[u]:
        if v != p[u]:
            p[v] = u
            degree[v] -= 1
            dfs(v)
    h -= 1

def centro(u):
    global d, mayor, c
    temp.append(u)
    d += 1
    if d > mayor:
        mayor = d
        c = temp[mayor // 2]
    for v in grafo[u]:
        if v != p[u]:
            p[v] = u
            centro(v)
    d -= 1
    temp.pop()

def centro():
    for i in range(1, n+1):
        if degree[i] == 1:
            temp.append(i)
            v = grafo[i][0]
            centro(v)
            break

for i in range(1, n):
    in1, in2 = map(int, input().split())
    grafo[in1].append(in2)
    grafo[in2].append(in1)
    degree[in1] += 1
    degree[in2] += 1

centro()
p = defaultdict(int)
dfs(c)
if band:
    print("Yes")
else:
    print("No")


