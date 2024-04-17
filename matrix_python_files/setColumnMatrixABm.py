class Matrix:
    def __init__(self, data):
        self.data = data  

    def get_row_dimension(self):
        return len(self.data)

    def get_column_dimension(self):
        return len(self.data[0]) if self.data else 0

    def get_entry(self, row, col):
        return self.data[row][col]

    def set_entry(self, row, col, value):
        self.data[row][col] = value

    def check_column_index(self, index):
        if index < 0 or index >= len(self.data[0]):
            raise IndexError("Column index out of bounds")

    def set_column_matrix(self, column_index, column_matrix):
        self.check_column_index(column_index)
        num_rows = self.get_row_dimension()

        if column_matrix.get_row_dimension() != num_rows or column_matrix.get_column_dimension() != 1:
            raise MatrixDimensionMismatchException(column_matrix.get_row_dimension(), column_matrix.get_column_dimension(), num_rows, 1)

        for i in range(num_rows):
            self.set_entry(i, column_index, column_matrix.get_entry(i, 0))

# Example usage
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

column_matrix_data = [
    [10],
    [11],
    [12]
]

matrix = Matrix(matrix_data)
column_matrix = Matrix(column_matrix_data)
try:
    matrix.set_column_matrix(1, column_matrix)
    print("Updated Matrix:")
    for row in matrix.data:
        print(row)
except (IndexError, MatrixDimensionMismatchException) as e:
    print(e)
