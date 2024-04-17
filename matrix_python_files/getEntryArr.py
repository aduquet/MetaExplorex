class Matrix:
    def __init__(self, data):
        self.data = data

    def check_matrix_index(self, row, col):
        """ Checks if the specified indices are within the matrix dimensions. """
        if row < 0 or row >= len(self.data):
            raise IndexError("row index out of bounds")
        if col < 0 or col >= len(self.data[0]):
            raise IndexError("column index out of bounds")

    def get_entry(self, row, col):
        """ Returns the matrix entry at the specified row and column. """
        self.check_matrix_index(row, col)  
        return self.data[row][col]

# Example usage
matrix_data = [
    [1.5, 2.5, 3.5],
    [4.5, 5.5, 6.5],
    [7.5, 8.5, 9.5]
]

matrix = Matrix(matrix_data)
try:
    entry = matrix.get_entry(1, 2)  
    print(f"The entry at row 1, column 2 is {entry}.")
except IndexError as e:
    print(e)
