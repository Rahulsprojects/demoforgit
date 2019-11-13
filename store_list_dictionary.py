n = int(input())
dicti = {}
listi = []
for i in range(n):
    listi = input().split()
    for k in range(1, 4):
        listi[k] = float(listi[k])
    dicti[listi[0]] = listi[1:]         # New info for me: A dictionary can store a list too

print(format(float(sum(dicti[input()]))/float(3), '.2f'))
#print(dicti[input()])
