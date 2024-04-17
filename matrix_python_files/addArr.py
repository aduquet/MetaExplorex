class Array2DRowRealMatrix:
    def __init__(self, data):
        self.data = data

    def getRowDimension(self):
        return len(self.data)

    def getColumnDimension(self):
        return len(self.data[0]) if self.data else 0

    def add(self, other):
        if self.getRowDimension() != other.getRowDimension() or \
           self.getColumnDimension() != other.getColumnDimension():
            raise ValueError("Matrices are not addition compatible")

        row_dimension = self.getRowDimension()
        column_dimension = self.getColumnDimension()
        result_data = [[0 for _ in range(column_dimension)] for _ in range(row_dimension)]

        for i in range(row_dimension):
            row_data_self = self.data[i]
            row_data_other = other.data[i]
            row_data_result = result_data[i]
            for j in range(column_dimension):
                row_data_result[j] = row_data_self[j] + row_data_other[j]

        return Array2DRowRealMatrix(result_data)

matrix1 = Array2DRowRealMatrix([[1, 2], [3, 4]])
matrix2 = Array2DRowRealMatrix([[5, 6], [7, 8]])
result_matrix = matrix1.add(matrix2)

print("Resultant Matrix:")
for row in result_matrix.data:
    print(row)
