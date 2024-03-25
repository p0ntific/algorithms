def convert(m, n):
    if(m == n):
        return 0
    if(m > n):
        return m - n
    if(m <= 0 and n > 0):
        return -1
    if(n % 2 == 1):
        return 1 + convert(m, n + 1)
    else:
        return 1 + convert(m, n / 2)

m, n = [int(x) for x in input().split()]
print(int(convert(m, n)))
 