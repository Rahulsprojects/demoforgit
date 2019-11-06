'''d = {
    "csev": 4,
    "iges": 10
}
for k, v in d.items():
    print(k, v)

d = {
    "d": 10,
    "b": 5,
    "c": 18
}
d.items()
print((d.items()))
for k, v in sorted(d.items()):
    print(k, v)'''

c = {
    "a": 10,
    "b": 1,
    "c": 22
}
temp = []
for k, v in c.items():
    temp.append((v, k))

print(temp)

temp = sorted(temp, reverse=True)
print(temp)






