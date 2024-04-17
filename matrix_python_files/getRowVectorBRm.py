import numpy as np

class BlockMatrix:
    def __init__(self, blocks, rows, columns, block_rows, block_columns, block_width_func):
        self.blocks = blocks
        self.rows = rows
        self.columns = columns
        self.block_rows = block_rows
        self.block_columns = block_columns
        self.block_width_func = block_width_func

    def check_row_index(self, index):
        if index < 0 or index >= self.rows:
            raise IndexError("Row index out of bounds")

    def get_row_vector(self, row_index):
        self.check_row_index(row_index)  
        result_vector = np.zeros(self.columns)  

        block_row_index = row_index // 52
        within_block_row = row_index % 52

        result_column_index = 0
        for block_column_index in range(self.block_columns):
            block_width = self.block_width_func(block_column_index)
            block_index = block_row_index * self.block_columns + block_column_index
            block = self.blocks[block_index]

            start_index = within_block_row * block_width

            result_vector[result_column_index:result_column_index + block_width] = block[start_index:start_index + block_width]
            result_column_index += block_width

        return result_vector

def block_width_func(block_column_index):
    return 52  

# Example usage
blocks = [
    np.array([i + j for i in range(52) for j in range(52)]) for _ in range(9) 
]

matrix = BlockMatrix(blocks, 156, 156, 3, 3, block_width_func)
try:
    row_vector = matrix.get_row_vector(53)  
    print("Row Vector:", row_vector)
except IndexError as e:
    print(e)
