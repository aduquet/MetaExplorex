class BlockMatrix:
    def __init__(self, blocks, block_rows, block_columns, block_width_func):
        self.blocks = blocks
        self.block_rows = block_rows
        self.block_columns = block_columns
        self.block_width_func = block_width_func

    def check_matrix_index(self, row, col):
        if row < 0 or row >= self.block_rows * 52 or col < 0 or col >= self.block_columns * 52:
            raise IndexError("Matrix index is out of bounds")

    def multiply_entry(self, row, col, scalar):
        self.check_matrix_index(row, col)

        block_row_index = row // 52
        block_col_index = col // 52

        within_block_row = row % 52
        block_width = self.block_width_func(block_col_index)
        within_block_col = col % 52

        block_index = block_row_index * self.block_columns + block_col_index
        element_index = within_block_row * block_width + within_block_col

        self.blocks[block_index][element_index] *= scalar

def block_width_func(col_index):
    return 52

# Example usage
blocks = [
    [1] * 52 * 52 for _ in range(9)  
]

matrix = BlockMatrix(blocks, 3, 3, block_width_func)
try:
    matrix.multiply_entry(53, 53, 10)  # Multiply the element at position (53,53) by 10
    print("Multiplication performed.")
except IndexError as e:
    print(e)
