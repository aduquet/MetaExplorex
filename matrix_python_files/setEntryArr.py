import numpy as np

class BlockRealMatrix:
    def __init__(self, data):
        self.data = np.array(data)
    
    def check_matrix_index(self, row_index, column_index):
        if not (0 <= row_index < self.data.shape[0] and 0 <= column_index < self.data.shape[1]):
            raise IndexError("Matrix index out of bounds.")
    
    def set_entry(self, row_index, column_index, value):
        self.check_matrix_index(row_index, column_index)
        self.data[row_index, column_index] = value

# Usage example
matrix = BlockRealMatrix([[1, 2], [3, 4]])
matrix.set_entry(1, 0, 5)
print(matrix.data)
