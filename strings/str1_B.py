with open("unequal.in", "r") as f:
    s = f.readline().strip()
    
class Block:
    def __init__(self):
        self.isSubStr = False
        self.letters = [0 for _ in range (26)]
 
n = len(s)
answer = 0
root = Block()

for i in range(n):
    node = root

    for j in range(i, n):
        id = ord(s[j]) - ord("a")

        if not node.letters[id]:
            node.letters[id] = Block()
            node.isSubStr = True
            answer += 1

        node = node.letters[id]


with open("unequal.out", "w") as f:
    f.write(str(answer))