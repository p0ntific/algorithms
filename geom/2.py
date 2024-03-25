answers = []
with open('intersec4.in', 'r') as f:   
    n = int(f.readline())
    for i in range(n):
        [x1,y1,r1] = [int(x) for x in f.readline().split()]
        [x2,y2,r2] = [int(x) for x in f.readline().split()]
        if(x1 == x2 and y1 == y2 and r1 == r2):
            answers.append(
                {
                    'point1':[x1,y1,r1],
                    'point1':[x2,y2,r2],
                    'cnt':3,
                }
            )
        elif((x1-x2)**2 + (y1-y2) == (r1 + r2)**2):
            answers.append(
                {
                    'point1':[x1,y1,r1],
                    'point1':[x2,y2,r2],
                    'cnt':1,
                }
            )
        elif((x1-x2)**2 + (y1-y2) <= (r1 + r2)**2):
            answers.append(
                {
                    'point1':[x1,y1,r1],
                    'point1':[x2,y2,r2],
                    'cnt':2,
                }
            )
        else:
            answers.append(
                {
                    'point1':[x1,y1,r1],
                    'point1':[x2,y2,r2],
                    'cnt':0,
                }
            )  

for ans in answers:
    cnt = ans['cnt']
    print(cnt)
    if(cnt == 1):
        pass 
    if(cnt == 2):
        pass 
        
with open('intersec4.out', 'w') as f: 
    
    ... 
    # f.write(str(length) + "\n")
    # for i in ans:
    #     f.write(str(points[i][0]) + " " + str(points[i][1]) + "\n")

