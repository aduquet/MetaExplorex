import numpy as np

class BlockRealMatrix:
    def __init__(self, data):
        if data is None:
            raise ValueError("The matrix data must not be null.")
        self.data = np.array(data)
    
    def set_sub_matrix(self, sub_matrix, start_row, start_col):
        if sub_matrix is None:
            raise ValueError("Sub-matrix must not be null.")
        
        sub_matrix = np.array(sub_matrix)
        sub_row_count, sub_col_count = sub_matrix.shape
        
        if sub_row_count == 0:
            raise ValueError("Sub-matrix must contain at least one row.")
        if sub_col_count == 0:
            raise ValueError("Sub-matrix must contain at least one column.")
        
        self.check_index(start_row, start_col, sub_row_count, sub_col_count)
        
        end_row = start_row + sub_row_count
        end_col = start_col + sub_col_count
        
        if end_row > self.data.shape[0] or end_col > self.data.shape[1]:
            raise IndexError("Sub-matrix does not fit within the dimensions of the original matrix.")
        
        self.data[start_row:end_row, start_col:end_col] = sub_matrix

    def check_index(self, start_row, start_col, num_rows, num_cols):
        if start_row < 0 or start_row >= self.data.shape[0]:
            raise IndexError("Start row index out of bounds.")
        if start_col < 0 or start_col >= self.data.shape[1]:
            raise IndexError("Start column index out of bounds.")
        if start_row + num_rows > self.data.shape[0]:
            raise IndexError("Sub-matrix extends beyond the number of rows.")
        if start_col + num_cols > self.data.shape[1]:
            raise IndexError("Sub-matrix extends beyond the number of columns.")

# Example usage
matrix = BlockRealMatrix(np.zeros((10, 10)))
sub_matrix = [[1, 2], [3, 4]]
matrix.set_sub_matrix(sub_matrix, 2, 3)
print(matrix.data)
