n = int(input())
lst = []
for i in range(n):
    query = input().split()
    cmd = query[0]
    arg = query[1:]
    if cmd == 'print':
        print(lst)
    else:
        cmd += '(' + ','.join(arg) + ')'
        eval("lst." + cmd)

