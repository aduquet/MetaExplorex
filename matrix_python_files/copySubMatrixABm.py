class Matrix:
    def __init__(self, data):
        self.data = data

    def checkSubMatrixIndex(self, selected_rows, selected_columns):
        pass

    def getEntry(self, row, column):
        return self.data[row][column]

    def copySubMatrix(self, selected_rows, selected_columns, destination):
        self.checkSubMatrixIndex(selected_rows, selected_columns)

        if len(destination) < len(selected_rows) or len(destination[0]) < len(selected_columns):
            raise MatrixDimensionMismatchException(len(destination), len(destination[0]), len(selected_rows), len(selected_columns))

        for i, row in enumerate(selected_rows):
            for j, column in enumerate(selected_columns):
                destination[i][j] = self.getEntry(row, column)

class MatrixDimensionMismatchException(Exception):
    def __init__(self, expected_rows, expected_columns, actual_rows, actual_columns):
        message = f"Expected dimensions: {expected_rows}x{expected_columns}, but got: {actual_rows}x{actual_columns}"
        super().__init__(message)

# Example usage
matrix_data = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]
matrix = Matrix(matrix_data)
selected_rows = [0, 2]  
selected_columns = [1, 2]  
destination = [[0, 0], [0, 0]]  

matrix.copySubMatrix(selected_rows, selected_columns, destination)
print(destination)  
