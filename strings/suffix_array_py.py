class SUFFIX_ARRAY:
    s = ''
    ranks = []
    def __init__(self, s) -> None:
        self.s = s
    
    
    def set_rank(self, arr):
        ranks = dict()
        i = 0
        for item in arr:
            if not ranks.get(item, None):
                ranks.update({item : i})
                i += 1

        self.ranks = ranks

    def solve(self):
        s = self.s
        arr = [ord(s[i]) for i in range(len(s))]

        k = 1
        tmp = []
        for i in range(len(arr)):
            if i + k < len(arr):
                tmp.append((arr[i], arr[i+k],))
            else:
                tmp.append((arr[i], -1,))

        sorted_tmp = sorted(tmp)
        self.set_rank(sorted_tmp)
        arr = [self.ranks[item] for item in tmp]
    
        while len(set(arr)) < len(arr):
            k *= 2
            tmp = []
        
            for i in range(len(arr)):
                if i + k < len(arr):
                    tmp.append((arr[i], arr[i+k],))
                else:
                    tmp.append((arr[i], -1,))
        
            sorted_tmp = sorted(tmp)
            self.set_rank(sorted_tmp)
            arr = [self.ranks[x] for x in tmp]

        self.set_rank(arr)
        arr = [self.ranks[i]+1 for i in range(len(arr))]
    
        return arr

with open('suffarray.in') as f:
    s = f.readline().strip()
    
sa = SUFFIX_ARRAY(s)
ans = sa.solve()

with open('suffarray.out', "w") as f:
    f.write(" ".join(map(str, ans)))
