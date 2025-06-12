# Assumes matrix input
def transpose(matrix):
    new_matrix = []
    for _ in matrix[0]:
        new_matrix.append(['' for ind in matrix])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]
print(transpose(matrix_3_by_5) == expected_result)