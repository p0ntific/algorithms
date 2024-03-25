
class BadTerritory:
    visited = set()
    pits = []
    
    def __init__(self, n, m, k, road):
        self.n = n
        self.m = m
        self.k = k
        self.road = road

    def fillThePits(self, dot):
        stack = [dot]
        pits = set([dot])
        is_good = False
        while stack:
            x, y = stack.pop()
            if (x == 0) or (x == (self.n - 1)) or (y == 0) or (y == (self.m - 1)):
                # в прошлом варианте не работали варианты вида:
                # 0..
                # ... 
                is_good = True
            # как в озерах
            for d in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                dx,dy = d
                if (0 <= dx < self.n) and (0 <= dy < self.m) and (d not in self.visited) and (self.road[dx][dy] == '.') and ( d not in pits):
                    self.visited.add(d)
                    pits.add(d)
                    stack.append(d)

        return is_good, pits

    def solve(self):
        for i in range(self.n):
            for j in range(self.m):
                # не яма или не нужно
                if self.road[i][j] == '*' or (i, j) in self.visited:
                    continue
                
                is_good, pits = self.fillThePits((i, j))

                if not is_good:
                    self.pits.append(pits)

        self.pits = sorted(self.pits, key=lambda x: len(x))

        cnt = 0
        for i in range(len(self.pits) - self.k):
            for x, y in self.pits[i]:
                self.road[x][y] = '*'
                cnt += 1

        return cnt, self.road

def main():
    road = []
    # with open("pits.in") as f:
    #     n, m, k = map(int, f.readline().strip().split())
    #     for _ in range(n):
    #         row = list(f.readline().strip())
    #         road.append(row)
            
    n, m, k = map(int, input().strip().split())

    for _ in range(n):
        row = list(input().strip())
        road.append(row)

    bt = BadTerritory(n, m, k, road)
    ans, road = bt.solve()

    # строки дороги
    print(ans)
    for i in road:
        print(''.join(i))

if __name__ == "__main__":
    main()
