m = 0
s = ""
P = 31
pPows = []
hash = []

def getHash(l, r):
    return hash[r + 1] - hash[l] * pows[r - l + 1]

def checkTwoSubs(a, b, c, d):
    return getHash(a, b) == getHash(c, d)

f1 = open('substrcmp.in', 'r')
f2 = open('substrcmp.out', 'w')
s = f1.readline().strip() 
m = int(f1.readline().strip() )
hash = [0] * (len(s) + 1)
pows = [0] * (len(s) + 1)
hash[0] = 0
pows[0] = 1

for i in range(len(s)):
    hash[i + 1] = hash[i] * P + ord(s[i])
    pows[i + 1] = pows[i] * P

for i in range(m):
    a, b, c, d = map(int, f1.readline().strip().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if checkTwoSubs(a, b, c, d):
        f2.write("Yes\n")
    else:
        f2.write("No\n")
f1.close()
f2.close()
