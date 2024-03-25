[n,m] = [int(x) for x in input().split()]

cnt=0
while(n*2<=m):
    n*=2
    cnt+=1

if(n < m):
    n*=2
    cnt +=1     

while(n != m):
    n -= 1
    cnt+=1

    
print(cnt)