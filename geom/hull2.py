import math
 
 
def get_intersections(first_circle, second_circle):
    x1, y1, r1 = first_circle
    x2, y2, r2 = second_circle
    
    if (x1 == x2 and y1 == y2 and r1 == r2):
        return -1
    
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if d > r1 + r2 or d < abs(r1 - r2):
        return []
    
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    x3 = x1 + (x2 - x1) * a / d
    y3 = y1 + (y2 - y1) * a / d
    
    h = math.sqrt(r1**2 - a**2)
    
    px1 = x3 + h * (y2 - y1) / d
    py1 = y3 - h * (x2 - x1) / d
    px2 = x3 - h * (y2 - y1) / d
    py2 = y3 + h * (x2 - x1) / d
    
    if px1 == px2 and py1 == py2: return [(px1, py2)]
    else: return [(px1, py1), (px2, py2)]
 
f1 = open("intersec4.in", "r")

f2 = open("intersec4.out", "w")

n = int(f1.readline())

for _ in range(n):
    circle1 = [int(i) for i in f1.readline().split()]
    circle2 = [int(i) for i in f1.readline().split()]
    
    intersections = get_intersections(circle1, circle2)
    
    if intersections == -1:
        f2.write("3\n")
        
    elif len(intersections) == 0:
        f2.write("0\n")
        
    elif len(intersections) == 1:
        f2.write("1\n")
        f2.write(str(intersections[0][0]) + " " + str(intersections[0][1]) + "\n")
        
    elif len(intersections) == 2:
        f2.write("2\n")
        
        x1 = (intersections[0][0] + intersections[1][0])*1.0/2
        y1 = (intersections[0][1] + intersections[1][1])*1.0/2
        x2 = circle1[0]
        y2 = circle1[1]
        
        f2.write(str(x1) + " " + str(y1) + "\n")
    
        f2.write(str(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) + " " + str(math.sqrt((intersections[0][0] - x1)**2 + (intersections[0][1] - y1) ** 2)) + "\n")
        
        f2.write(str(intersections[0][0]) + " " + str(intersections[0][1]) + "\n")
        f2.write(str(intersections[1][0]) + " " + str(intersections[1][1]) + "\n")
