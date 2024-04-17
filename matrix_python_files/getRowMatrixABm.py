class Matrix:
    def __init__(self, data):
        self.data = data

    def check_row_index(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Row index out of bounds")

    def get_column_dimension(self):
        return len(self.data[0]) if self.data else 0

    def get_entry(self, row, col):
        return self.data[row][col]

    def create_matrix(self, rows, cols):
        return Matrix([[0] * cols for _ in range(rows)])

    def set_entry(self, row, col, value):
        self.data[row][col] = value

    def get_row_matrix(self, row_index):
        self.check_row_index(row_index)  
        column_dimension = self.get_column_dimension()
        row_matrix = self.create_matrix(1, column_dimension)  

        for col in range(column_dimension):
            value = self.get_entry(row_index, col)
            row_matrix.set_entry(0, col, value)

        return row_matrix

# Example usage
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = Matrix(matrix_data)
try:
    row_matrix = matrix.get_row_matrix(1)
    print("Row Matrix:", row_matrix.data)  # Expected to show the second row: [[4, 5, 6]]
except IndexError as e:
    print(e)
