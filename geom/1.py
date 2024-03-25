import random
import math

def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def polar_angle(p0, p1 = None):
    if p1 is None:
        p1 = anchor
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return math.atan2(y_span, x_span)
 
 
def distance(p0, p1 = None):
    if p1 is None:
        p1 = anchor
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return y_span**2 + x_span**2
 
 
def quicksort(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    piv_ang = polar_angle(a[random.randint(0, len(a) - 1)])
    for pt in a:
        pt_ang = polar_angle(pt)
        if pt_ang < piv_ang:
            smaller.append(pt)
        elif pt_ang == piv_ang:
            equal.append(pt)
        else:
            larger.append(pt)
    return quicksort(smaller) + sorted(equal, key=distance) + quicksort(larger)

points = []

with open('hull.in', 'r') as f:   
    n = int(f.readline())
    for i in range(n):
        points.append([int(x) for x in f.readline().split()])
        
points = list(set(tuple(sub) for sub in points))

ids = [i for i in range(n)]

for i in range(1,n):
    if points[ids[i]][0]<points[ids[0]][0]:
        ids[i], ids[0] = ids[0], ids[i] 


for i in range(2,n): 
    j = i
    while j>1 and (rotate(points[ids[0]],points[ids[j-1]],points[ids[j]])<0): 
        ids[j], ids[j-1] = ids[j-1], ids[j]
        j -= 1
        
ans = [ids[0],ids[1]]

for i in range(2,n):
    while rotate(points[ans[-2]],points[ans[-1]],points[ids[i]])<=0:
        del ans[-1] 
        if len(ans)<2:
            break
    ans.append(ids[i])

length = len(ans)

with open('hull.out', 'w') as f:   
    f.write(str(length) + "\n")
    for i in ans:
        f.write(str(points[i][0]) + " " + str(points[i][1]) + "\n")

