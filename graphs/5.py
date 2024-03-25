with open("cycle2.in", "r") as f:
    [n, m] = [int(x) for x in f.readline().strip().split()]
    g = [[] for _ in range(n+1)]
    used = [0] * (n+1)
    flag = 0
    path = []

    def dfs(v):
        global flag
        if flag == 1:
            return
        used[v] = 1
        path.append(v)
        for to in g[v]:
            if used[to] == 1:
                path.append(to)
                flag = 1
                return
            else:
                dfs(to)
            if flag == 1:
                return
        used[v] = 2
        path.pop()

    for _ in range(m):
        a,b = [int(x) for x in f.readline().strip().split()]
        g[a].append(b)

    for i in range(1, n+1):
        if used[i] == 0:
            dfs(i)
            if flag == 1:
                break
    with open("cycle2.out", "w") as f2:
        if flag == 1:
            i = len(path) - 2
            to = path[-1]
            while path[i] != to:
                i -= 1
            f2.write("YES\n")
            f2.write(' '.join([str(x) for x in path[i:-1]]))
        else:
            f2.write("NO")

