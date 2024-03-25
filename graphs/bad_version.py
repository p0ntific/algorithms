import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class TanksSolver:
    def __init__(self):
        # with open('tanks.in') as f:
        #     self.n, self.p = map(int, f.readline().split())
        #     self.graph = [list(map(int, f.readline().split())) for _ in range(self.p)]
        self.n, self.p = [int(x) for x in input().split()]    
        self.graph = [list(map(int, input().split())) for _ in range(self.p)]
        self.tanksIn = [[] for _ in range(self.n)]
        self.tanksOut = [[] for _ in range(self.n)]

    def fill(self):
        for node in self.graph:
            self.tanksIn[node[1] - 1].append(node[0])
            self.tanksOut[node[0] - 1].append((node[1], node[2]))

    def solve(self):
        self.fill()
        ans = []
        for x in range(self.n):
            if not self.tanksIn[x] and self.tanksOut[x]:
                start, d, end = x + 1, self.tanksOut[x][0][1], self.tanksOut[x][0][0]
                while self.tanksOut[end - 1]:
                    d = min(d, self.tanksOut[end - 1][0][1])
                    end = self.tanksOut[end - 1][0][0]
                ans.append(f"{start} {end} {d}")
        return f"{len(ans)}\n" + "\n".join(ans)

if __name__ == "__main__":
    ts = TanksSolver()
    print(ts.solve())
