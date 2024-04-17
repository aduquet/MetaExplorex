class BlockRealMatrix:
    def __init__(self, total_rows, total_columns, block_size=52):
        self.total_rows = total_rows
        self.total_columns = total_columns
        self.block_size = block_size
        self.block_rows = (total_rows + block_size - 1) // block_size 
        self.block_columns = (total_columns + block_size - 1) // block_size
        self.blocks = [
            [float(i + j) for j in range(block_size) for i in range(block_size)]
            for _ in range(self.block_rows * self.block_columns)
        ]

    def checkColumnIndex(self, column):
        if column < 0 or column >= self.total_columns:
            raise IndexError("Column index out of bounds")

    def getColumn(self, column_index):
        self.checkColumnIndex(column_index)
        column_data = [0.0] * self.total_rows
        block_column = column_index // self.block_size
        column_in_block = column_index % self.block_size

        for block_row in range(self.block_rows):
            block = self.blocks[block_row * self.block_columns + block_column]
            for i in range(min(self.block_size, self.total_rows - block_row * self.block_size)):
                column_data[block_row * self.block_size + i] = block[i * self.block_size + column_in_block]

        return column_data

# Example usage:
total_rows = 105  
total_columns = 105  
matrix = BlockRealMatrix(total_rows, total_columns)
column_data = matrix.getColumn(5)
print(column_data) 
