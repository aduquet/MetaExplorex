class SparseMatrix:
    def __init__(self):
        self.entries = {}  
        
    def check_row_index(self, row):
        if row < 0 or row > 100:
            raise IndexError("Row index is out of bounds")

    def check_column_index(self, col):
        if col < 0 or col > 100:
            raise IndexError("Column index is out of bounds")

    def compute_key(self, row, col):
        return (row, col)

    def multiply_entry(self, row, col, scalar):
        self.check_row_index(row)
        self.check_column_index(col)

        key = self.compute_key(row, col)
        current_value = self.entries.get(key, 0)  
        new_value = current_value * scalar

        if new_value != 0:
            self.entries[key] = new_value  
        else:
            self.entries.pop(key, None)  

# Example usage
matrix = SparseMatrix()
matrix.entries[(1, 2)] = 3  
matrix.multiply_entry(1, 2, 5)  

matrix.multiply_entry(1, 2, 0)  

print("Updated entries:", matrix.entries)
