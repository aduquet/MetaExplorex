import numpy as np

class BlockRealMatrix:
    def __init__(self, blocks, block_size=52):
        self.blocks = [[np.array(block) for block in row] for row in blocks]
        self.block_size = block_size
        self.block_rows = len(blocks)
        self.block_columns = len(blocks[0])
    
    def check_row_index(self, index):
        total_rows = self.block_rows * self.block_size
        if not (0 <= index < total_rows):
            raise IndexError("Row index out of bounds.")
    
    def get_column_dimension(self):
        return sum(block.shape[1] for block in self.blocks[0])
    
    def block_width(self, block_column_index):
        return self.blocks[0][block_column_index].shape[1]
    
    def set_row(self, row_index, new_values):
        self.check_row_index(row_index)
        if len(new_values) != self.get_column_dimension():
            raise ValueError("Dimension mismatch: the provided array does not match the total number of columns.")
        
        row_block_index = row_index // self.block_size
        local_row_index = row_index % self.block_size
        
        start_col_index = 0
        for block_index in range(self.block_columns):
            block_width = self.block_width(block_index)
            end_col_index = start_col_index + block_width
            self.blocks[row_block_index][block_index][local_row_index, :] = new_values[start_col_index:end_col_index]
            start_col_index = end_col_index

# Example usage
block_data = [
    [np.zeros((52, 10)) for _ in range(3)], 
    [np.zeros((52, 10)) for _ in range(3)]
]
matrix = BlockRealMatrix(block_data)
new_row = np.arange(30)  
matrix.set_row(53, new_row) 

print("Updated row in block 1:", matrix.blocks[1][0][1, :])  
