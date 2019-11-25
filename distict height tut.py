n = int(input())
height = map(int, input().split())
height = list(set(height))
entities = len(height)
tot_heights = 0
for i in height:
    tot_heights += i
print(tot_heights/entities)


