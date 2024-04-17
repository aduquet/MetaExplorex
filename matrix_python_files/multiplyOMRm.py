class OpenMapRealMatrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.entries = {}  

    def check_multiplication_compatible(self, other):
        if self.columns != other.rows:
            raise ValueError("Matrices are not multiplication compatible.")

    def compute_key(self, row, col):
        return row * self.columns + col

    def multiply(self, other):
        self.check_multiplication_compatible(other)
        result_matrix = OpenMapRealMatrix(self.rows, other.columns)

        for (row, col), value in self.entries.items():
            for k in range(other.columns):
                other_key = (col, k)
                if other_key in other.entries:
                    result_key = (row, k)
                    product = value * other.entries[other_key]
                    if result_key in result_matrix.entries:
                        result_matrix.entries[result_key] += product
                    else:
                        result_matrix.entries[result_key] = product
                    if result_matrix.entries[result_key] == 0:
                        del result_matrix.entries[result_key]

        return result_matrix

# Example usage
matrix_a = OpenMapRealMatrix(3, 2)
matrix_a.entries[(0, 1)] = 3
matrix_a.entries[(1, 0)] = 5

matrix_b = OpenMapRealMatrix(2, 3)
matrix_b.entries[(1, 0)] = 2
matrix_b.entries[(1, 2)] = 4

result = matrix_a.multiply(matrix_b)
print("Resulting Matrix Entries:")
for key, value in result.entries.items():
    print(f"Position {key}: Value {value}")