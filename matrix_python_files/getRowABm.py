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

    def get_row(self, row_index):
        self.check_row_index(row_index)  
        column_dimension = self.get_column_dimension()
        row_data = [0] * column_dimension  

        for i in range(column_dimension):
            row_data[i] = self.get_entry(row_index, i)

        return row_data

# Example usage
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = Matrix(matrix_data)
try:
    row = matrix.get_row(1)  
    print("Row:", row)
except IndexError as e:
    print(e)
