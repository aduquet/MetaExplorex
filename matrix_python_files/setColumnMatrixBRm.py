import numpy as np

class BlockRealMatrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.row_dimension = self.data.shape[0]
        self.column_dimension = self.data.shape[1]
    
    def get_row_dimension(self):
        return self.row_dimension

    def check_column_index(self, index):
        if not (0 <= index < self.column_dimension):
            raise IndexError("Column index out of bounds.")
    
    def set_column_matrix(self, column_index, column_matrix):
        self.check_column_index(column_index)
        
        if column_matrix.get_row_dimension() != self.get_row_dimension():
            raise ValueError("Matrix dimension mismatch.")
        
        if column_matrix.column_dimension != 1:
            raise ValueError("Input must be a single column matrix.")
        
        self.data[:, column_index] = column_matrix.data[:, 0]

# Usage example
matrix = BlockRealMatrix([[1, 2], [3, 4]])
new_column = BlockRealMatrix([[5], [6]])
matrix.set_column_matrix(1, new_column)
print(matrix.data)
