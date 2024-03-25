class Prefix_suffix_solver:
    
    z = []
    ans = ''
    ans_len = 0
    
    def __init__(self, s) -> None:
        self.s = s
        self.n = len(s)

    def zFunction(self):
        z = [0] * self.n
        l = r = 0
        for i in range(1, self.n):
            if i > r:
                l = r = i
                while r < self.n and self.s[r - l] == self.s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < self.n and self.s[r - l] == self.s[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
        self.z = z

    def solve(self):
        self.zFunction()
        self.z[0] = self.n
        zCopy = sorted(self.z)
        ln = 0
        ans = ""
        for i in range(self.n):
            if self.z[self.n - i - 1] != i + 1:
                continue
            ln += 1
            count = len(zCopy) - zCopy.index(i + 1)
            ans += str(i + 1) + " " + str(count) + "\n"
        self.ans = ans
        self.ans_len = ln
        self.ans_len = ln
        
    def print_ans(self):
        print(self.ans_len)
        print(self.ans)

s=input().strip()
solver = Prefix_suffix_solver(s)
solver.solve()
solver.print_ans()

