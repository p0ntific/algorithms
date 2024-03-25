class FUN:
    s_1 = 0
    s_0 = 0
    t_1 = 0
    t_0 = 0
    ans = ''
    
    def __init__(self, s, t) -> None:
        self.s = s
        self.t = t
    
    def count_in_main_string(self) -> None:
        for c in self.s:
            if c == '1':
                self.s_1 += 1 
            else:
                self.s_0 += 1
                
    def count_in_pattern(self) -> None:
        for c in self.t:
            if c == '1':
                self.t_1 += 1 
            else:
                self.t_0 += 1
                
    def solve(self) -> str:
        self.count_in_main_string()
        self.count_in_pattern()
        self.get_max_suf_pref()
        if(self.s_1 >= self.t_1 and self.s_0 >= self.t_0):
            self.ans += self.t
            self.s_1 -= self.t_1 
            self.s_0 -= self.t_0
            
        self.t_1 -= self.pref_suf_1
        self.t_0 -= self.pref_suf_0
        
        while(self.s_1 >= self.t_1 and self.s_0 >= self.t_0):
            self.ans += self.t[self.pref_suf:]
            self.s_1 -= self.t_1 
            
            self.s_0 -= self.t_0
            
        for _ in range(self.s_1):
            self.ans += '1'
        for _ in range(self.s_0):
            self.ans += '0'
            
        return self.ans
    

        
s = input().strip()
t = input().strip()
fun = FUN(s,t)        
print(fun.solve())