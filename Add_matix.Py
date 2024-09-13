matrix1=[
    [1,2,3],
    [1,1,1],
    [0,2,1]
    ]
matrix2=[
    [1,1,0],
    [1,2,1],
    [0,2,0]
    ]
result=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]+=matrix1[i][j] +matrix2[i][j]
for r in result:
    print(r)
