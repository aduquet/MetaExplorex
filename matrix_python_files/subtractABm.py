import numpy as np

class RealMatrix:
    def __init__(self, data):
        self.data = np.array(data)
    
    def get_row_dimension(self):
        return self.data.shape[0]
    
    def get_column_dimension(self):
        return self.data.shape[1]
    
    def get_entry(self, row, col):
        return self.data[row, col]
    
    def set_entry(self, row, col, value):
        self.data[row, col] = value
    
    def create_matrix(self, rows, cols):
        return RealMatrix(np.zeros((rows, cols)))
    
    def check_subtraction_compatible(self, other):
        if self.get_row_dimension() != other.get_row_dimension() or self.get_column_dimension() != other.get_column_dimension():
            raise ValueError("Matrices dimensions must match for subtraction.")
    
    def subtract(self, other):
        self.check_subtraction_compatible(other)
        result = self.create_matrix(self.get_row_dimension(), self.get_column_dimension())
        
        for i in range(self.get_row_dimension()):
            for j in range(self.get_column_dimension()):
                result.set_entry(i, j, self.get_entry(i, j) - other.get_entry(i, j))
        
        return result

# Example usage
matrix1 = RealMatrix([[1, 2], [3, 4]])
matrix2 = RealMatrix([[1, 0], [0, 1]])
result_matrix = matrix1.subtract(matrix2)
print(result_matrix.data)
