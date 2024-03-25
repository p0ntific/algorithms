class CheckSub:
    
    z = []
    
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

    def search(self, pattern):
        concat = pattern + "$" + self.s
        self.s = concat
        self.n = len(concat)
        self.zFunction()
        good = False
        
        for i in range(self.n):
            if self.z[i] == len(pattern):
                return 1
            
        if not good:
            return 0

with open('dictionary.in') as f:
    s = f.readline().strip()
    n = int(f.readline().strip())
    solver = CheckSub(s)
    ans = []
    for _ in range(n):
        t = f.readline().strip()
        ans.append(solver.search(t))

with open('dictionary.out', "w") as f:
    for i in ans:
        f.write("Yes\n" if i else "No\n")