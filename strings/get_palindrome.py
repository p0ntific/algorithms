class GET_PALINDROME:
    s = ''
    ans = ''
    
    def __init__(self, s) -> None:
        self.s = s 
        
    
    def find(self, s) -> str:
        
        s = s[:] + "#" + s[::-1]
        n = len(s)
        
        max_palindrome = [0]*n
        max_palindrome[0] = 0
        
        i = 1
        cnt = 0
        
        while(i < n):
            if s[i] == s[cnt]:
                cnt += 1
                max_palindrome[i] = cnt
                i += 1
            else:
                if cnt != 0:
                    cnt = max_palindrome[cnt - 1]
                else:
                    max_palindrome[i] = 0
                    i += 1
                    
        return s[:max_palindrome[n-1]]
        
    def solve(self):
        s = self.s
        n = len(s)
        i = 0
        j = n - 1
        
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        
        str1 = ""
        str2 = ""
        str3 = ""
        
        if i > 0:
            str1 = s[0: i]
            str2 = s[n - i: n]
        
        if n > 2 * i:
            copy = s[i: n - i]
            pal1 = self.find(copy)
            pal2 = self.find(copy[::-1])
            
            str3 = pal1 if len(pal1) > len(pal2) else pal2
            
        self.ans = str1 + str3 + str2
        
        
        
    def print_ans(self):
        print(self.ans)



def findPalindrome(C):
    S = C[::-1]
 
    C = C[:] + '&' + S
 
    n = len(C)
    longestPalindrome = [0 for i in range(n)]
    longestPalindrome[0] = 0
 
    ll = 0
    i = 1
 
    while (i < n):
        if (C[i] == C[ll]):
            ll += 1
            longestPalindrome[i] = ll
            i += 1
 
        else:
 
            if (ll != 0):
                ll = longestPalindrome[ll - 1]
            else:
                longestPalindrome[i] = 0
                i += 1
 
    ans = C[0:longestPalindrome[n - 1]]
 
    return ans
 
 
def findAns(s):
 
    A = ""
    B = ""
    F = ""
 
    i = 0
    j = len(s) - 1
    ll = len(s)
    while (i < j and s[i] == s[j]):
        i = i + 1
        j = j - 1
 
    if (i > 0):
        A = s[0: i]
        B = s[ll - i: ll]
 
    if (ll > 2 * i):
 
        C = s[i: i + (len(s) - 2 * i)]
        D = findPalindrome(C)
        C = C[::-1]
        E = findPalindrome(C)
 
        if (len(D) > len(E)):
            F = D
        else:
            F = E
 
    answer = A + F + B
 
    return answer

n = int(input())
for _ in range(n):
    s = input().strip()
    solver = GET_PALINDROME(s)
    solver.solve()
    solver.print_ans()