import math

class BlockMatrix:
    def __init__(self, blocks, block_rows, block_columns, block_width_func):
        self.blocks = blocks
        self.block_rows = block_rows
        self.block_columns = block_columns
        self.block_width_func = block_width_func

    def check_matrix_index(self, row, col):
        """ Checks if the specified indices are within the dimensions defined by block structure. """
        total_rows = self.block_rows * 52  
        total_columns = self.block_columns * 52  
        if row < 0 or row >= total_rows:
            raise IndexError("Row index out of bounds")
        if col < 0 or col >= total_columns:
            raise IndexError("Column index out of bounds")

    def get_entry(self, row, col):
        self.check_matrix_index(row, col)

        block_row = row // 52
        block_col = col // 52

        local_row = row % 52
        local_col = col % 52

        block_index = block_row * self.block_columns + block_col

        if block_index >= len(self.blocks):
            raise IndexError("Block index out of range")

        block = self.blocks[block_index]

        block_size = 52
        block_2d = [block[i:i+block_size] for i in range(0, len(block), block_size)]

        local_index = local_row * self.block_width_func(block_col) + local_col

        return block_2d[local_row][local_col]

# Example usage
blocks = [
    [0] * 52 * 52,  
    [0] * 52 * 52,  
    [0] * 52 * 52,  
    [0] * 52 * 52,  
    [0] * 52 * 52,  
    [0] * 52 * 52,  
    [0] * 52 * 52,  
    [0] * 52 * 52,  
    [0] * 52 * 52,  
]
matrix = BlockMatrix(blocks, 3, 3, lambda x: 52)
try:
    entry = matrix.get_entry(53, 53)  
    print(entry)
except IndexError as e:
    print(e)
