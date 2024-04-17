def add_matrices(matrix_data1, matrix_data2):
    if len(matrix_data1) != len(matrix_data2) or len(matrix_data1[0]) != len(matrix_data2[0]):
        raise ValueError("Matrices are not addition compatible")

    row_dimension = len(matrix_data1)
    column_dimension = len(matrix_data1[0])
    result_matrix = [[0 for _ in range(column_dimension)] for _ in range(row_dimension)]

    for i in range(row_dimension):
        for j in range(column_dimension):
            result_matrix[i][j] = matrix_data1[i][j] + matrix_data2[i][j]

    return result_matrix

# Test the function
matrix_data1 = [[1, 2], [3, 4]]
matrix_data2 = [[5, 6], [7, 8]]
result_matrix_data = add_matrices(matrix_data1, matrix_data2)

print("Resultant Matrix:")
for row in result_matrix_data:
    print(row)
