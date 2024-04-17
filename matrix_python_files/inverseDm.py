class DiagonalMatrix:
    def __init__(self, data):
        self.data = data  

    def is_singular(self, tolerance):
        return any(abs(x) <= tolerance for x in self.data)

    def inverse(self, tolerance=0.0):
        if self.is_singular(tolerance):
            raise ValueError("Matrix is singular to working precision.")

        inverse_data = [1.0 / x for x in self.data]

        return DiagonalMatrix(inverse_data)

# Example usage
diagonal_elements = [1, 2, 3, 4] 
matrix = DiagonalMatrix(diagonal_elements)
try:
    inv_matrix = matrix.inverse()
    print("Inverted Matrix:", inv_matrix.data)
except ValueError as e:
    print(e)
