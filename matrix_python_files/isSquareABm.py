class Matrix:
    def __init__(self, data):
        self.data = data

    def get_column_dimension(self):
        return len(self.data[0]) if self.data else 0

    def get_row_dimension(self):
        return len(self.data)

    def is_square(self):
        return self.get_row_dimension() == self.get_column_dimension()

# Example usage
matrix_data_square = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_data_not_square = [
    [1, 2, 3],
    [4, 5, 6]
]

square_matrix = Matrix(matrix_data_square)
not_square_matrix = Matrix(matrix_data_not_square)

print("Is the matrix square (square matrix)?", square_matrix.is_square())  # Expected: True
print("Is the matrix square (not square matrix)?", not_square_matrix.is_square())  # Expected: False
