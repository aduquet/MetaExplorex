class SparseRealMatrix:
    def __init__(self):
        self.entries = {}

    def computeKey(self, row, column):
        return f"{row},{column}"

    def checkRowIndex(self, row):
        pass

    def checkColumnIndex(self, column):
        pass

    def addToEntry(self, row, column, value):
        self.checkRowIndex(row)
        self.checkColumnIndex(column)

        key = self.computeKey(row, column)

        existing_value = self.entries.get(key, 0.0)
        new_value = existing_value + value

        if new_value != 0.0:
            self.entries[key] = new_value
        else:
            if key in self.entries:
                del self.entries[key]

# Example usage
matrix = SparseRealMatrix()
matrix.addToEntry(1, 2, 5.0)
matrix.addToEntry(1, 2, -3.0)
matrix.addToEntry(1, 2, -2.0)
print(matrix.entries)
