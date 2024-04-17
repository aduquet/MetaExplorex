import numpy as np

class BlockRealMatrix:
    def __init__(self, blocks, block_size=52):
        self.blocks = [[np.array(block) for block in row_blocks] for row_blocks in blocks]
        self.block_size = block_size
        self.block_rows = len(blocks)
        self.block_columns = len(blocks[0])

    def get_row_dimension(self):
        return len(self.blocks[0][0]) if self.blocks else 0

    def get_column_dimension(self):
        return sum([block.shape[1] for block in self.blocks[0]])

    def check_row_index(self, index):
        total_rows = self.block_rows * self.block_size
        if not (0 <= index < total_rows):
            raise IndexError("Row index out of bounds.")
    
    def block_width(self, block_column_index):
        return self.blocks[0][block_column_index].shape[1]
    
    def set_row_matrix(self, row_index, row_matrix):
        self.check_row_index(row_index)
        if row_matrix.get_row_dimension() != 1:
            raise ValueError("Input matrix must have exactly one row.")
        if row_matrix.get_column_dimension() != self.get_column_dimension():
            raise ValueError("Column dimension mismatch.")

        row_block_index = row_index // self.block_size
        local_row_index = row_index % self.block_size
        
        start_col_index = 0
        for block_index in range(self.block_columns):
            block_width = self.block_width(block_index)
            end_col_index = start_col_index + block_width
            row_data = row_matrix.blocks[0][block_index]
            self.blocks[row_block_index][block_index][local_row_index, :block_width] = row_data[0, :]
            start_col_index = end_col_index

# Example usage
blocks = [
    [np.zeros((52, 10)) for _ in range(3)],  
    [np.zeros((52, 10)) for _ in range(3)]
]
row_blocks = [
    [[np.ones(10) * 5], [np.ones(10) * 6], [np.ones(10) * 7]]
]
matrix = BlockRealMatrix(blocks)
row_matrix = BlockRealMatrix(row_blocks, block_size=52)
matrix.set_row_matrix(53, row_matrix) 
print("Updated row in block 1, second block:", matrix.blocks[1][1][1, :])  