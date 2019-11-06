rec = dict()
for i in range(int(input())):
    d = input().split()
    rec[d[0]] = rec.get(d[0], 0) + (int(d[1]) + int(d[2]) + int(d[3]))/3
name = input()
for k, v in rec.items():
    if k == name:
        print("%.2f" % float(v))
