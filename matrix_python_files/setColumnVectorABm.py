import numpy as np

class RealVector:
    def __init__(self, elements):
        self.elements = np.array(elements)
        
    def get_dimension(self):
        return len(self.elements)

    def get_entry(self, index):
        return self.elements[index]

class BlockRealMatrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.row_dimension = self.data.shape[0]
        self.column_dimension = self.data.shape[1]
    
    def get_row_dimension(self):
        return self.row_dimension
    
    def check_column_index(self, index):
        if not (0 <= index < self.column_dimension):
            raise IndexError("Column index out of bounds.")

    def set_column_vector(self, column_index, vector):
        self.check_column_index(column_index)
        if vector.get_dimension() != self.get_row_dimension():
            raise ValueError("Matrix dimension mismatch: vector dimension does not match matrix row dimension.")
        
        for i in range(vector.get_dimension()):
            self.data[i, column_index] = vector.get_entry(i)

# Usage example
matrix = BlockRealMatrix([[1, 2], [3, 4]])
vector = RealVector([5, 6])
matrix.set_column_vector(1, vector)
print(matrix.data)
