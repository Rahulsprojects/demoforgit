from collections import Counter

myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
d = Counter(myList)
print(d.items())

for k, v in d.items():
    print(k, v)
