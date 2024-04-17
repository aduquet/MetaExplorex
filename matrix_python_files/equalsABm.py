class RealMatrix:
    def __init__(self, data):
        self.data = data

    def getRowDimension(self):
        return len(self.data)

    def getColumnDimension(self):
        return len(self.data[0]) if self.data else 0

    def getEntry(self, row, column):
        return self.data[row][column]

    def equals(self, other):
        if self is other:
            return True

        if not isinstance(other, RealMatrix):
            return False

        if other.getRowDimension() != self.getRowDimension() or other.getColumnDimension() != self.getColumnDimension():
            return False

        for i in range(self.getRowDimension()):
            for j in range(self.getColumnDimension()):
                if self.getEntry(i, j) != other.getEntry(i, j):
                    return False

        return True

# Example usage:
matrix1 = RealMatrix([[1, 2], [3, 4]])
matrix2 = RealMatrix([[1, 2], [3, 4]])
matrix3 = RealMatrix([[4, 5], [6, 7]])

print(matrix1.equals(matrix2))  
print(matrix1.equals(matrix3)) 
print(matrix1.equals("not a matrix")) 
