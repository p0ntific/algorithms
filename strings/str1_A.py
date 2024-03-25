def pi(s):
    p = [0]
    for i in range(1, len(s)):
        j = p[i - 1]
        while (j > 0 and s[i] != s[j]):
            j = p[j - 1]
        if (s[i] == s[j]):
            j = j + 1
        p.append(j)
    
    return p

with open("search.in", "r") as f:
    a = f.readline().strip()
    b = f.readline().strip()
    s = b + "#" + a
    p = pi(s)

    with open("search.out", "w") as f:
        f.write(str(p.count(len(b))) + "\n")
        for i in range(len(p)):
            if (p[i] == len(b)):
                f.write(str(i - 2 * len(b) + 1) + " ")

