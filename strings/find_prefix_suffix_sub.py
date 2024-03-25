class SUB_SOLVER:
    MAX_N = 10**5 + 10
    arr = [0] * MAX_N
    sort_arr = [0] * MAX_N
    ans = []
    
    def __init__(self, string):
        self.s = string
        
    def fill_arr(self):
        l = 0
        r = 0
        n = len(self.s)
        self.arr[0] = n
        
        for i in range(1, n):
            if i > r:
                l = i
                r = i
                while r < n and self.s[r - l] == self.s[r]:
                    r += 1
                self.arr[i] = r - l
                r -= 1
            else:
                k = i - l
                if self.arr[k] < r - i + 1:
                    self.arr[i] = self.arr[k]
                else:
                    l = i
                    while r < n and self.s[r - l] == self.s[r]:
                        r += 1
                    self.arr[i] = r - l

    def solve(self):
        self.fill_arr()
        for i in range(len(s)):
            self.sort_arr[i] = self.arr[i]
        self.sort_arr.sort()
        for i in range(len(self.s) - 1, -1, -1):
            if i + self.arr[i] == len(self.s):
                count = len(self.sort_arr) - self.sort_arr.index(self.arr[i])
                self.ans.append((self.arr[i], count))

    def get_ans(self):
        print(len(self.ans))
        for i in self.ans:
            print(i[0], i[1])
        
s = input().strip()

solver = SUB_SOLVER(s)

solver.solve()

solver.get_ans()


