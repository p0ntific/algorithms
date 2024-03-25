
    
with open("substrcmp.in", "r") as f:
    s = f.readline().strip()
    m = int(f.readline().strip())
    for i in range(m):
        a,b,c,d =[int(x) for x in f.readline().strip().split()]
        if b-a != d-c:
            print("NO")
            continue
        # проверяем хэши
        if hash(s[a:b]) == hash(s[c:d]):
            if(s[a:b] == s[c:d]):
                print("YES")

            