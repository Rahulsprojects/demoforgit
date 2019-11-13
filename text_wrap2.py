# without using textwrap
s = input()
w = int(input())
for i in range(0, len(s)+1, w):
    print(s[i:(i+w)])

