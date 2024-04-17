import numpy as np

class BlockRealMatrix:
    def __init__(self, data):
        self.data = np.array(data)
    
    def check_not_null(self, obj, message):
        if obj is None:
            raise ValueError(message)
    
    def check_row_index(self, index):
        if index < 0 or index >= self.data.shape[0]:
            raise IndexError("Row index out of bounds.")
    
    def check_column_index(self, index):
        if index < 0 or index >= self.data.shape[1]:
            raise IndexError("Column index out of bounds.")
    
    def check_matrix_dimensions(self, matrix):
        if matrix.size == 0:
            raise ValueError("Matrix must contain at least one element.")
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise ValueError("All rows in the matrix must have the same length.")
    
    def set_sub_matrix(self, sub_matrix, start_row, start_col):
        self.check_not_null(sub_matrix, "Sub-matrix must not be null.")
        sub_matrix = np.array(sub_matrix)
        self.check_matrix_dimensions(sub_matrix)
        
        self.check_row_index(start_row)
        self.check_column_index(start_col)
        
        end_row = start_row + sub_matrix.shape[0]
        end_col = start_col + sub_matrix.shape[1]
        
        self.check_row_index(end_row - 1)
        self.check_column_index(end_col - 1)
        
        self.data[start_row:end_row, start_col:end_col] = sub_matrix

# Example usage
matrix = BlockRealMatrix(np.zeros((10, 10)))
sub_matrix = [[1, 2], [3, 4]]
matrix.set_sub_matrix(sub_matrix, 2, 3)
print(matrix.data)
