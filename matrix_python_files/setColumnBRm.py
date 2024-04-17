class MatrixDimensionMismatchException(Exception):
    def __init__(self, provided_rows, provided_cols, expected_rows, expected_cols):
        message = f"Dimension mismatch: provided ({provided_rows}x{provided_cols}), expected ({expected_rows}x{expected_cols})"
        super().__init__(message)

class BlockMatrix:
    def __init__(self, data, rows, columns, block_size=52):
        self.data = data  
        self.rows = rows
        self.columns = columns
        self.block_size = block_size
        self.block_rows = (rows + block_size - 1) // block_size
        self.block_columns = (columns + block_size - 1) // block_size

    def check_column_index(self, index):
        if index < 0 or index >= self.columns:
            raise IndexError("Column index out of bounds")

    def get_row_dimension(self):
        return self.rows

    def block_width(self, block_index):
        if (block_index + 1) * self.block_size > self.columns:
            return self.columns % self.block_size
        return self.block_size

    def block_height(self, block_row):
        if (block_row + 1) * self.block_size > self.rows:
            return self.rows % self.block_size
        return self.block_size

    def set_column(self, column_index, column_data):
        self.check_column_index(column_index)
        if len(column_data) != self.get_row_dimension():
            raise MatrixDimensionMismatchException(len(column_data), 1, self.get_row_dimension(), 1)

        block_col = column_index // self.block_size
        col_in_block = column_index % self.block_size

        data_index = 0
        for block_row in range(self.block_rows):
            block = self.data[block_row * self.block_columns + block_col]
            block_height = self.block_height(block_row)

            for i in range(block_height):
                block[i][col_in_block] = column_data[data_index]
                data_index += 1

# Example usage
blocks = [[[0 for _ in range(52)] for _ in range(52)] for _ in range(4)]  
matrix = BlockMatrix(blocks, 104, 104)
column_data = [i for i in range(104)]  

try:
    matrix.set_column(1, column_data)  # Set second column with new data
    print("Column set successfully.")
except Exception as e:
    print(e)
