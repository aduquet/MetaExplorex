class Matrix:
    def __init__(self, data):
        self.data = data

    def get_row_dimension(self):
        return len(self.data)

    def get_column_dimension(self):
        return len(self.data[0]) if self.data else 0

    def get_entry(self, row, col):
        return self.data[row][col]

    def create_matrix(self, rows, cols):
        return Matrix([[0] * cols for _ in range(rows)])

    def set_entry(self, row, col, value):
        self.data[row][col] = value

    def scalar_add(self, scalar):
        num_rows = self.get_row_dimension()
        num_cols = self.get_column_dimension()
        result_matrix = self.create_matrix(num_rows, num_cols)

        for i in range(num_rows):
            for j in range(num_cols):
                entry = self.get_entry(i, j)
                new_value = entry + scalar
                result_matrix.set_entry(i, j, new_value)

        return result_matrix

# Example usage
matrix_data = [
    [1, 2],
    [3, 4]
]

matrix = Matrix(matrix_data)
scalar_value = 5
result_matrix = matrix.scalar_add(scalar_value)

print("Original Matrix:")
for row in matrix.data:
    print(row)

print("Matrix after Scalar Addition:")
for row in result_matrix.data:
    print(row)
