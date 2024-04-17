class SparseMatrix:
    def __init__(self, data, rows, columns):
        self.data = data 
        self.rows = rows
        self.columns = columns

    def is_square(self):
        return self.rows == self.columns

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError("Matrices are not multiplication compatible.")

        result_data = {}
        for (i, k), v in self.data.items():
            for j in range(other.columns):
                if (k, j) in other.data:
                    if (i, j) in result_data:
                        result_data[(i, j)] += v * other.data[(k, j)]
                    else:
                        result_data[(i, j)] = v * other.data[(k, j)]
        return SparseMatrix(result_data, self.rows, other.columns)

    def copy(self):
        return SparseMatrix(dict(self.data), self.rows, self.columns)

    def power(self, exponent):
        if exponent < 0:
            raise ValueError("Exponent must be non-negative.")
        if not self.is_square():
            raise ValueError("Matrix must be square to be raised to a power.")

        if exponent == 0:
            return SparseMatrix({(i, i): 1 for i in range(self.rows)}, self.rows, self.columns)
        elif exponent == 1:
            return self.copy()

        result = self.copy()
        power = self.copy()
        for bit in bin(exponent)[3:]: 
            power = power.multiply(power)  
            if bit == '1':
                result = result.multiply(power)
        
        return result

# Example usage
matrix_data = {
    (0, 0): 1,
    (1, 1): 2,
    (2, 2): 3
}
matrix = SparseMatrix(matrix_data, 3, 3)
try:
    result_matrix = matrix.power(3)
    print("Matrix raised to power 3:", result_matrix.data)
except ValueError as e:
    print(e)
