s = input()
width = int(input())
p = []
while len(s) > width:
    for i in range(width):
        p.append(s[i])
    print("".join(p))
    p = []
    s = s[width:]
    if len(s) < width:
        p.append(s)
        print(*p)










