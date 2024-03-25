class Solver:
    s = ''
    prefix = []
    
    def __init__(self, s) -> None:
        self.s = s
        self.n = len(s)
        self.tree = 
        
    def prefix_function(self):
        s = self.s
        v = [0]*len(s)
        for i in range(1,len(s)):
            k = v[i-1]
            while k > 0 and s[k] != s[i]:
                k = v[k-1]
            if s[k] == s[i]:
                k = k + 1
            v[i] = k
        self.prefix = v
    
    def build_tree():
        
    
    def print_data(self):
        print(self.s)
        print(self.prefix)
        

solver = Solver('abacabadava')
