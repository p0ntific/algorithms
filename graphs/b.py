import io
import os
 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
    
q = int(input())
for _ in range(q):
    ans = 0
    v = 0
    
    n, m = map(int, input().split())
    lake = [[*map(int, input().split())] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if lake[i][j]:
                queue = [(i, j)]
                v = 0
                while queue:
                    x, y = queue.pop()
                    v += lake[x][y]
                    lake[x][y] = 0
                    for t in range(4):
                        #
                        if 0 <= x + dx[t] < n and 0 <= y + dy[t] < m:
                            if lake[x + dx[t]][y + dy[t]]:
                                queue.append((x + dx[t], y + dy[t]))
            ans = max(ans, v)
            
    print(ans)