import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
parents = [0] * n

for i in range (n):
    parents[i] = int(input())
    
ans = 0
for i in range(n):
    villager = i
    cnt = 1
    while parents[villager] != -1:
        villager = parents[villager]
        cnt += 1
    ans = max(cnt,ans)

print(ans)
