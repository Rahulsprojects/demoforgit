x, y, z, n = (int(input()) for l in range(4))
threed_grid = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                threed_grid.append([i, j, k])
# print(threed_grid)
for rows in threed_grid:
    print(rows)






