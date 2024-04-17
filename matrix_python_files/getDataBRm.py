import math

class BlockMatrix:
    def __init__(self, blocks, rows, columns, block_rows, block_columns):
        self.blocks = blocks 
        self.rows = rows
        self.columns = columns
        self.block_rows = block_rows
        self.block_columns = block_columns

    def get_data(self):
        block_size = 52 

        total_block_rows = math.ceil(self.rows / block_size)
        total_block_columns = math.ceil(self.columns / block_size)

        full_matrix = [[0] * self.columns for _ in range(self.rows)]

        for block_row in range(total_block_rows):
            row_start = block_row * block_size
            row_end = min((block_row + 1) * block_size, self.rows)

            for block_col in range(total_block_columns):
                col_start = block_col * block_size
                col_end = min((block_col + 1) * block_size, self.columns)

                block_index = block_row * total_block_columns + block_col
                block = self.blocks[block_index]

                block_num_rows = len(block)

                for i in range(row_end - row_start):
                    if i < block_num_rows: 
                        block_row_length = len(block[i])
                        for j in range(col_end - col_start):
                            if j < block_row_length:  
                                full_matrix[row_start + i][col_start + j] = block[i][j]

        return full_matrix

# Example usage
blocks = [
    [[1, 2], [3, 4]],  
    [[5, 6], [7, 8]],  
    [[9, 10], [11, 12]],
    [[13, 14], [15, 16]]
]
matrix = BlockMatrix(blocks, 4, 4, 2, 2)
data = matrix.get_data()
for row in data:
    print(row)
