import numpy as np

class Array2DRowRealMatrix:
    def __init__(self, data, copy=True):
        if copy:
            self.data = np.array(data, dtype=float)
        else:
            self.data = data
    
    def get_row_dimension(self):
        return self.data.shape[0]
    
    def get_column_dimension(self):
        return self.data.shape[1]
    
    def check_subtraction_compatible(self, other):
        if self.get_row_dimension() != other.get_row_dimension() or self.get_column_dimension() != other.get_column_dimension():
            raise ValueError("Matrix dimensions must be the same for subtraction.")
    
    def subtract(self, other):
        self.check_subtraction_compatible(other)
        
        result_data = self.data - other.data
        return Array2DRowRealMatrix(result_data, copy=False)

# Example usage
matrix1 = Array2DRowRealMatrix([[1, 2], [3, 4]])
matrix2 = Array2DRowRealMatrix([[1, 0], [0, 1]])
result_matrix = matrix1.subtract(matrix2)
print(result_matrix.data)