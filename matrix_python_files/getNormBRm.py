import math

class BlockMatrix:
    def __init__(self, blocks, block_rows, block_columns, block_width_func, block_height_func):
        self.blocks = blocks
        self.block_rows = block_rows
        self.block_columns = block_columns
        self.block_width_func = block_width_func
        self.block_height_func = block_height_func

    def get_norm(self):
        max_norm = 0.0
        block_widths = [self.block_width_func(i) for i in range(self.block_columns)]
        for col_index in range(self.block_columns):
            row_sums = [0.0] * block_widths[col_index]
            for block_row_index in range(self.block_rows):
                block_index = block_row_index * self.block_columns + col_index
                block = self.blocks[block_index]
                block_height = self.block_height_func(block_row_index)
                for i in range(block_widths[col_index]):
                    sum_abs = 0.0
                    for j in range(block_height):
                        index = j * block_widths[col_index] + i
                        sum_abs += abs(block[index])
                    row_sums[i] += sum_abs
            max_norm = max(max_norm, max(row_sums))
        return max_norm

def block_width_func(index):
    return 52 

def block_height_func(index):
    return 52  

# Example usage
blocks = [
    [abs(i - j) for i in range(52) for j in range(52)],
    [abs(i - j) for i in range(52) for j in range(52)],
    [abs(i - j) for i in range(52) for j in range(52)],
    [abs(i - j) for i in range(52) for j in range(52)],
    [abs(i - j) for i in range(52) for j in range(52)],
    [abs(i - j) for i in range(52) for j in range(52)],
    [abs(i - j) for i in range(52) for j in range(52)],
    [abs(i - j) for i in range(52) for j in range(52)],
    [abs(i - j) for i in range(52) for j in range(52)]
]

matrix = BlockMatrix(blocks, 3, 3, block_width_func, block_height_func)
norm = matrix.get_norm()
print("Matrix Norm:", norm)
