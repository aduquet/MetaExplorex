import numpy as np

class BlockRealMatrix:
    def __init__(self, rows, columns, block_size=52):
        self.block_size = block_size
        self.block_rows = (rows + block_size - 1) // block_size
        self.block_cols = (columns + block_size - 1) // block_size
        self.blocks = [np.zeros((block_size, block_size)) for _ in range(self.block_rows * self.block_cols)]
    
    def _block_index(self, block_row, block_col):
        return block_row * self.block_cols + block_col
    
    def set_sub_matrix(self, sub_matrix, start_row, start_col):
        sub_matrix = np.array(sub_matrix)
        sub_rows, sub_cols = sub_matrix.shape
        
        if sub_rows == 0 or sub_cols == 0:
            raise ValueError("Sub-matrix must not be empty.")
        
        end_row = start_row + sub_rows
        end_col = start_col + sub_cols
        
        self._check_sub_matrix_indices(start_row, end_row, start_col, end_col)
        
        for i in range(sub_rows):
            for j in range(sub_cols):
                global_row = start_row + i
                global_col = start_col + j
                
                block_row = global_row // self.block_size
                block_col = global_col // self.block_size
                
                within_block_row = global_row % self.block_size
                within_block_col = global_col % self.block_size
                
                block_idx = self._block_index(block_row, block_col)
                self.blocks[block_idx][within_block_row, within_block_col] = sub_matrix[i, j]
    
    def _check_sub_matrix_indices(self, start_row, end_row, start_col, end_col):
        if start_row < 0 or start_row >= end_row or end_row > self.block_size * self.block_rows:
            raise IndexError("Row indices out of bounds.")
        if start_col < 0 or start_col >= end_col or end_col > self.block_size * self.block_cols:
            raise IndexError("Column indices out of bounds.")

# Example usage
matrix = BlockRealMatrix(200, 200) 
sub_matrix = [[1, 2, 3], [4, 5, 6]]
matrix.set_sub_matrix(sub_matrix, 50, 50)  

block_index = matrix._block_index(1, 1)  
print(matrix.blocks[block_index])
