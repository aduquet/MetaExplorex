class RealMatrix:
    def createMatrix(self, row_count, column_count):
        return Array2DRowRealMatrix(row_count, column_count)

class Array2DRowRealMatrix:
    def __init__(self, row_count, column_count):
        self.data = [[0.0 for _ in range(column_count)] for _ in range(row_count)]

# Example usage:
matrix_factory = RealMatrix()
new_matrix = matrix_factory.createMatrix(3, 5)
print(new_matrix.data)  
