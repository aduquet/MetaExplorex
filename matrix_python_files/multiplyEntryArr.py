class Matrix:
    def __init__(self, data):
        self.data = data

    def check_matrix_index(self, row, col):
        if row < 0 or row >= len(self.data) or col < 0 or col >= len(self.data[0]):
            raise IndexError("Matrix index is out of bounds")

    def multiply_entry(self, row, col, scalar):
        self.check_matrix_index(row, col)  
        self.data[row][col] *= scalar  

# Example usage
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix = Matrix(matrix_data)
try:
    matrix.multiply_entry(1, 1, 10)  # Multiply the element at (1,1), which is 5, by 10
    print("Updated Matrix:")
    for row in matrix.data:
        print(row)
except IndexError as e:
    print(e)
