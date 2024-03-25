def pi(s) :
    l = len(s)
    P = [0]*l
    i, j = 0, 1
    while j < l :
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        elif i:       
            i = P[i - 1]
        else:           
            P[j] = 0
            j += 1
    return P


str = input().strip()
n = len(str)
ans = []
cnt = 0
print(pi(str))
print(pi(''.join(reversed(str))))
        
# print(cnt+1)
# for i in ans:
#     print(i[0],i[1])
# print(n,1)
    