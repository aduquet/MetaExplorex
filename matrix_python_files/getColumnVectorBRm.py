class BlockRealMatrix:
    def __init__(self, blocks, rows, cols, block_size=52):
        self.blocks = blocks
        self.rows = rows
        self.cols = cols
        self.block_size = block_size
        self.block_rows = (rows + block_size - 1) // block_size
        self.block_columns = (cols + block_size - 1) // block_size

    def checkColumnIndex(self, column):
        if column < 0 or column >= self.cols:
            raise IndexError("Column index out of bounds")

    def blockWidth(self, block_column_index):
        return min(self.block_size, self.cols - block_column_index * self.block_size)

    def blockHeight(self, block_row_index):
        return min(self.block_size, self.rows - block_row_index * self.block_size)

    def getColumnVector(self, column_index):
        self.checkColumnIndex(column_index)
        vector_data = [0.0] * self.rows
        block_col_index = column_index // self.block_size
        col_in_block = column_index % self.block_size

        for block_row_index in range(self.block_rows):
            block_index = block_row_index * self.block_columns + block_col_index
            block = self.blocks[block_index]
            block_height = self.blockHeight(block_row_index)
            for i in range(block_height):
                vector_data[block_row_index * self.block_size + i] = block[i * self.block_size + col_in_block]

        return ArrayRealVector(vector_data)

class ArrayRealVector:
    def __init__(self, data):
        self.data = data

# Example usage
blocks = [[0] * 52 * 52 for _ in range(4)]  
matrix = BlockRealMatrix(blocks, 104, 104)  
column_vector = matrix.getColumnVector(3)  
print(column_vector.data)
