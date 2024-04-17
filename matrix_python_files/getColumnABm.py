class RealMatrix:
    def __init__(self, data):
        self.data = data

    def getRowDimension(self):
        return len(self.data)

    def checkColumnIndex(self, index):
        if index < 0 or index >= len(self.data[0]):
            raise IndexError("Column index out of bounds")

    def getEntry(self, row, column):
        return self.data[row][column]

    def getColumn(self, column_index):
        self.checkColumnIndex(column_index)
        row_dimension = self.getRowDimension()
        column_data = [0] * row_dimension  

        for i in range(row_dimension):
            column_data[i] = self.getEntry(i, column_index)

        return column_data

# Example usage:
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = RealMatrix(matrix_data)
print(matrix.getColumn(1))  
