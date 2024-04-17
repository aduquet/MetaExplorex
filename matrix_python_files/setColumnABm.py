class MatrixDimensionMismatchException(Exception):
    def __init__(self, provided_rows, provided_cols, expected_rows, expected_cols):
        message = f"Dimension mismatch: provided ({provided_rows}x{provided_cols}), expected ({expected_rows}x{expected_cols})"
        super().__init__(message)

class Matrix:
    def __init__(self, data):
        self.data = data

    def get_row_dimension(self):
        return len(self.data)

    def check_column_index(self, index):
        if index < 0 or index >= len(self.data[0]):
            raise IndexError("Column index out of bounds")

    def set_column(self, column_index, column_data):
        self.check_column_index(column_index)
        num_rows = self.get_row_dimension()

        if len(column_data) != num_rows:
            raise MatrixDimensionMismatchException(len(column_data), 1, num_rows, 1)

        for i in range(num_rows):
            self.data[i][column_index] = column_data[i]

# Example usage
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_column_data = [10, 11, 12]

matrix = Matrix(matrix_data)
try:
    matrix.set_column(1, new_column_data)
    print("Updated Matrix:")
    for row in matrix.data:
        print(row)
except (IndexError, MatrixDimensionMismatchException) as e:
    print(e)
