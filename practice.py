import collections
x = int(input())
shoes = collections.Counter(map(int, input().split()))
income = 0
for i in range(int(input())):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1
print(income)


