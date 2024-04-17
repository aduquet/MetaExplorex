class RealMatrix:
    def __init__(self, data):
        self.data = data

    def checkMatrixIndex(self, row, column):
        if row < 0 or row >= self.getRowDimension() or column < 0 or column >= self.getColumnDimension():
            raise IndexError("Matrix index is out of bounds")

    def getRowDimension(self):
        return len(self.data)

    def getColumnDimension(self):
        return len(self.data[0]) if self.data else 0

    def addToEntry(self, row, column, increment):
        self.checkMatrixIndex(row, column)
        self.data[row][column] += increment

matrix = RealMatrix([[1, 2], [3, 4]])
matrix.addToEntry(0, 1, 5)  
print(matrix.data)  