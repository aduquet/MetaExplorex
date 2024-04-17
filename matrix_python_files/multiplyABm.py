class Matrix:
    def __init__(self, data):
        self.data = data

    def get_row_dimension(self):
        return len(self.data)

    def get_column_dimension(self):
        return len(self.data[0]) if self.data else 0

    def get_entry(self, row, col):
        return self.data[row][col]

    def create_matrix(self, rows, cols):
        return Matrix([[0] * cols for _ in range(rows)])

    def set_entry(self, row, col, value):
        self.data[row][col] = value

    def multiply(self, other):
        if self.get_column_dimension() != other.get_row_dimension():
            raise ValueError("Matrices are not compatible for multiplication.")
        
        result = self.create_matrix(self.get_row_dimension(), other.get_column_dimension())

        for i in range(self.get_row_dimension()):
            for j in range(other.get_column_dimension()):
                sum_product = 0.0
                for k in range(self.get_column_dimension()):
                    sum_product += self.get_entry(i, k) * other.get_entry(k, j)
                result.set_entry(i, j, sum_product)

        return result

# Example usage
matrix_a_data = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b_data = [
    [7, 8],
    [9, 10],
    [11, 12]
]

matrix_a = Matrix(matrix_a_data)
matrix_b = Matrix(matrix_b_data)

try:
    result_matrix = matrix_a.multiply(matrix_b)
    for row in result_matrix.data:
        print(row)
except ValueError as e:
    print(e)
