class Matrix:
    def __init__(self, data):
        self.data = data

    def get_row_dimension(self):
        return len(self.data)

    def get_column_dimension(self):
        return len(self.data[0]) if self.data else 0

    def get_entry(self, row, col):
        return self.data[row][col]

    def get_trace(self):
        num_rows = self.get_row_dimension()
        num_columns = self.get_column_dimension()

        if num_rows != num_columns:
            raise ValueError("Matrix is not square ({}x{}). Trace can only be computed for square matrices.".format(num_rows, num_columns))

        trace = 0.0
        for i in range(num_rows):
            trace += self.get_entry(i, i)

        return trace

# Example usage
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = Matrix(matrix_data)
try:
    matrix_trace = matrix.get_trace()
    print("Trace of the matrix:", matrix_trace)
except ValueError as e:
    print(e)
