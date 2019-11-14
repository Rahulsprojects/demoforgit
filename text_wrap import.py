import textwrap
s = input()
w = int(input())
l = "\n".join(textwrap.wrap(s, w))
print(l)




'''








import textwrap

s = input()
w = int(input())
l = " ".join(textwrap.wrap(s, w))
print(textwrap.fill(l, w))
'''