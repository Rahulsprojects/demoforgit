n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(t.__hash__())





