import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
# print(shoes)
# print(shoes[5])
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print(income)
