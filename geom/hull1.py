import random
import math


def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])
 
 
def get_angle(p0, p1 = None):
    if p1 is None:
        p1 = anchor
    return math.atan2(p0[1] - p1[1], p0[0] - p1[0])
 
 
def rad(p0, p1 = None):
    if p1 is None:
        p1 = anchor
    return (p0[1] - p1[1])**2 + (p0[0] - p1[0])**2
 
 
def sort(a):
    if len(a) <= 1:
        return a
    smaller = []
    equal = []
    larger = []
    piv_ang = get_angle(a[random.randint(0, len(a) - 1)])
    for pt in a:
        pt_ang = get_angle(pt)
        if pt_ang < piv_ang:
            smaller.append(pt)
        elif pt_ang == piv_ang:
            equal.append(pt)
        else:
            larger.append(pt)
    return sort(smaller) + sorted(equal, key=rad) + sort(larger)
 
 
def get_hull(points):
    global anchor
 
    min_id = None
    for i, (x, y) in enumerate(points):
        if min_id == None or y < points[min_id][1] or (y == points[min_id][1] and x < points[min_id][0]):
            min_id = i
    anchor = points[min_id]
    points = sort(points)
    del points[points.index(anchor)]
 
    ans = [anchor, points[0]]
    for s in points[1:]:
        while rotate(ans[-2], ans[-1], s) <= 0:
            del ans[-1]  
            if len(ans) < 2: 
                break
        ans.append(s)
    return ans
 
ans = []
file = open("hull.in", "r")
n = int(file.readline())
points = []
for i in range(n):
    x = map(int, input().split())
    points.append(x)
file.close()
ans = get_hull(points)
    
file = open("hull.out", "w")
file.write(str(len(ans)) + "\n")
for i in range(len(ans)):
    file.write(str(ans[i][0]) + " " + str(ans[i][1]) + "\n")
file.close()
    