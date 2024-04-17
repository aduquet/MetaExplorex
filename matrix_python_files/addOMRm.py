from collections import defaultdict

class OpenMapRealMatrix:
    def __init__(self, matrix=None, rows=None, columns=None):
        if matrix:
            self.rows = matrix.rows
            self.columns = matrix.columns
            self.entries = dict(matrix.entries)
        else:
            self.rows = rows
            self.columns = columns
            self.entries = defaultdict(float)

    def getEntry(self, row, column):
        return self.entries.get((row, column), 0.0)

    def setEntry(self, row, column, value):
        self.entries[(row, column)] = value

    def add(self, other):
        result = OpenMapRealMatrix(self)

        for (key, value) in other.entries.items():
            row, column = key
            original_value = self.getEntry(row, column)
            result.setEntry(row, column, original_value + value)

        return result

matrix1 = OpenMapRealMatrix(rows=2, columns=2)
matrix1.setEntry(0, 1, 2)
matrix1.setEntry(1, 0, 3)

matrix2 = OpenMapRealMatrix(rows=2, columns=2)
matrix2.setEntry(0, 1, 5)
matrix2.setEntry(1, 0, 7)

result_matrix = matrix1.add(matrix2)

print("Resultant Matrix Entries:")
for key, value in result_matrix.entries.items():
    print(f"Position {key}: {value}")
