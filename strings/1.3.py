with open("palindrome.in", "r") as f:
    s = f.readline().strip()
    
n = len(s)

odd = [0] * n
even = [0] * n

l = 0
r = -1
for i in range(n):
    cur = 1
    # get in  border of right palindrome
    if i < r:
        cur = min(r - i + 1, odd[l + r - i])
    while i + cur < n and i - cur >= 0 and s[i - cur] == s[i + cur]:
        cur += 1
    odd[i] = cur
    # border of right palindrome
    if i + cur - 1 > r:
        l = i - cur + 1
        r = i + cur - 1

l = 0
r = -1
for i in range(n):
    cur = 0
    if i < r:
        cur = min(r - i + 1, even[l + r - i + 1])
    while i + cur < n and i - 1 - cur >= 0 and s[i - 1 - cur] == s[i + cur]:
        cur += 1
    even[i] = cur
    if i + cur - 1 > r:
        l = i - cur
        r = i + cur - 1

ans = 0
for i in range(n):
    if odd[i] > 1:
        ans += odd[i] - 1
    if even[i]:
        ans += even[i]

with open("palindrome.out", "w") as f:
    f.write(str(ans))

