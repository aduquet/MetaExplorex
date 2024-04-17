class Matrix:
    def __init__(self, data):
        self.data = data

    def get_row_dimension(self):
        if self.data is not None:
            return len(self.data)
        return 0

# Example usage
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

empty_matrix_data = []

matrix = Matrix(matrix_data)
empty_matrix = Matrix(empty_matrix_data)

print("Row dimension of matrix:", matrix.get_row_dimension())  # Expected output: 3
print("Row dimension of empty matrix:", empty_matrix.get_row_dimension())  # Expected output: 0
