import numpy as np

class BlockRealMatrix:
    def __init__(self, block_data, block_size=52):
        self.blocks = [[np.array(block) for block in row_blocks] for row_blocks in block_data]
        self.block_size = block_size
        self.block_rows = len(block_data)
        self.block_columns = len(block_data[0])
    
    def check_matrix_index(self, row_index, column_index):
        total_rows = self.block_rows * self.block_size
        total_columns = self.block_columns * self.block_size
        if not (0 <= row_index < total_rows and 0 <= column_index < total_columns):
            raise IndexError("Matrix index out of bounds.")
    
    def block_width(self, block_column_index):
        return self.blocks[0][block_column_index].shape[1]

    def set_entry(self, row_index, column_index, value):
        self.check_matrix_index(row_index, column_index)
        
        block_row_index = row_index // self.block_size
        block_column_index = column_index // self.block_size
        
        local_row_index = row_index % self.block_size
        local_column_index = column_index % self.block_size
        
        self.blocks[block_row_index][block_column_index][local_row_index, local_column_index] = value

# Example usage
block_data = [
    [np.zeros((52, 52)) for _ in range(3)], 
    [np.zeros((52, 52)) for _ in range(3)]
]
matrix = BlockRealMatrix(block_data)
matrix.set_entry(53, 105, 10)  
print("Value set at [53, 105]:", matrix.blocks[1][2][1, 1])
