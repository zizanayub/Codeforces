matrix = []

for i in range(5):
    row = list(map(int,input().split()))
    matrix.append(row)

    if 1 in row:
        x,y=i,row.index(1)

min_distance = abs(x-2) + abs(y-2)
print(min_distance)