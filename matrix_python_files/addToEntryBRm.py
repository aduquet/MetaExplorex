class BlockRealMatrix:
    def __init__(self, blocks, block_size=52):
        self.blocks = blocks  
        self.block_size = block_size 
        self.block_rows = len(blocks)
        self.block_columns = len(blocks[0]) if self.block_rows > 0 else 0

    def blockWidth(self, blockColumnIndex):
        return self.block_size

    def checkMatrixIndex(self, row, column):
        if row < 0 or column < 0:
            raise IndexError("Index out of bounds")

    def addToEntry(self, row, column, increment):
        self.checkMatrixIndex(row, column)
        block_row_index = row // self.block_size
        block_column_index = column // self.block_size
        row_in_block = row % self.block_size
        column_in_block = column % self.block_size
        block_index = block_row_index * self.block_columns + block_column_index
        block_width = self.blockWidth(block_column_index)
        index_in_block = row_in_block * block_width + column_in_block
        self.blocks[block_index][row_in_block][column_in_block] += increment