from itertools import combinations
s, n = input().split()
print(*["".join(i) for i in combinations(sorted(s))],sep="\n")