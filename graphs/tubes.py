class TanksSolver:
    ans = ''
    pipes = []
    def __init__(self):
        self.n_p = [int(x) for x in input().split(" ")]
        for _ in range(self.n_p[1]):
            self.pipes.append([int(x) for x in input().split(" ")])
        self.tanksIn = [[] for _ in range(self.n_p[0])]
        self.tanksOut = [[] for _ in range(self.n_p[0])]
        
    def fill(self):
        for pipe in self.pipes:
            self.In[pipe[1] - 1].append(pipe[0])
            self.tanksOut[pipe[0] - 1].append((pipe[1], pipe[2]))
        
    def solve(self):
        self.fill()
        ans = []
        for x in range(self.n_p[0]):
            if not self.tanksIn[x] and self.tanksOut[x]:
                start = x + 1
                d = self.tanksOut[x][0][1]
                end = self.tanksOut[x][0][0]
                while self.tanksOut[end - 1]:
                    d = min(d, self.tanksOut[end - 1][0][1])
                    end = self.tanksOut[end - 1][0][0]
                ans.append(str(start) + " " + str(end) + " " + str(d))
        return str(len(ans)) + "\n" + "\n".join(ans)

 
 
if __name__ == "__main__":
    ts = TanksSolver()
    print(ts.solve())