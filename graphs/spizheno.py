def filling(x, y):
    
    queue = [(x, y)]

    hole = set([(x, y)])
    ditch = False
    
    while queue:
        x, y = queue.pop()
        
        if (x == 0) or (x == (n-1)) or (y == 0) or (y == (m-1)):
            ditch = True
        
        for x_new, y_new in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if (0 <= x_new < n) and (0 <= y_new < m) and ((x_new, y_new) not in visited):
                if ((x_new, y_new) not in hole) and (field[x_new][y_new] == '.'):
                    visited.add((x_new, y_new))
                    hole.add((x_new, y_new))
                    queue.append((x_new, y_new))
    
    return ditch, hole

field = []
visited = set()
holes = []

with open("pits.in") as f:
    n, m, k = map(int, f.readline().strip().split())
    for _ in range(n):
        row = list(f.readline().strip())
        field.append(row)
    
for i in range(n):
    for j in range(m):
        
        if field[i][j] == '*' or (i, j) in visited:
            continue
        
        ditch, hole = filling(i, j)
        
        if not ditch: holes.append(hole)      
            
holes = sorted(holes, key = lambda x: len(x))
        
res = 0
for i in range(len(holes) - k):
    for x, y in holes[i]:
        res += 1
        field[x][y] = '*'

print(res)
for x in field:
    print(''.join(x))