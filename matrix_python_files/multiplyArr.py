class Array2DRowRealMatrix:
    def __init__(self, data):
        self.data = data

    def get_row_dimension(self):
        return len(self.data)

    def get_column_dimension(self):
        return len(self.data[0]) if self.data else 0

    def multiply(self, other):
        if self.get_column_dimension() != other.get_row_dimension():
            raise ValueError("Matrices are not multiplication compatible.")

        num_rows = self.get_row_dimension()
        num_cols = other.get_column_dimension()
        num_terms = self.get_column_dimension()

        result_data = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        for i in range(num_rows):
            for j in range(num_cols):
                sum_product = 0
                for k in range(num_terms):
                    sum_product += self.data[i][k] * other.data[k][j]
                result_data[i][j] = sum_product

        return Array2DRowRealMatrix(result_data)

    def __repr__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

# Example usage
matrix_a_data = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b_data = [
    [1, 4],
    [2, 5],
    [3, 6]
]

matrix_a = Array2DRowRealMatrix(matrix_a_data)
matrix_b = Array2DRowRealMatrix(matrix_b_data)

try:
    result_matrix = matrix_a.multiply(matrix_b)
    print("Result of Matrix Multiplication:")
    print(result_matrix)
except ValueError as e:
    print(e)
