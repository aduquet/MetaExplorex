class RealMatrix:
    def __init__(self, data):
        self.data = data

    def getRowDimension(self):
        return len(self.data)

    def getColumnDimension(self):
        return len(self.data[0]) if self.data else 0

    def checkColumnIndex(self, column):
        if column < 0 or column >= self.getColumnDimension():
            raise IndexError("Column index out of bounds")

    def getEntry(self, row, column):
        return self.data[row][column]

    def createMatrix(self, row_count, column_count):
        return [[0.0] * column_count for _ in range(row_count)]

    def setEntry(self, matrix, row, column, value):
        matrix[row][column] = value

    def getColumnMatrix(self, column_index):
        self.checkColumnIndex(column_index)
        row_dimension = self.getRowDimension()
        column_matrix = self.createMatrix(row_dimension, 1)  

        for i in range(row_dimension):
            entry = self.getEntry(i, column_index)
            self.setEntry(column_matrix, i, 0, entry)  

        return column_matrix

# Example usage:
matrix_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = RealMatrix(matrix_data)
column_matrix = matrix.getColumnMatrix(1)  
print(column_matrix)  