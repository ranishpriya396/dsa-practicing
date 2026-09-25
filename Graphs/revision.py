edges = [[1,2],[2,1],[2,3],[3,2],[4,1],[1,4]]
n = len(edges)
m = len(edges)-1
# matrix = [[0 for i in range(0,n)] for _ in range(0,n)]
matrix =[]
for _ in range(0,n):
    row = []
    for i in range(0,n):
        row.append(0)
    matrix.append(row)

# for row in matrix:
#     print(row)
#     print() 

for i, j in edges:
    matrix[i][j] = 1
    matrix[j][i] = 1
for row in matrix:
    print(row)
    print() 
# print(matrix)
