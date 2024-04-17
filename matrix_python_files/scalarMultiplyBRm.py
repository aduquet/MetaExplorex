class BlockRealMatrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.blocks = [[([0] * 52) for _ in range(52)] for _ in range((rows // 52 + 1) * (columns // 52 + 1))]

    def scalar_multiply(self, scalar):
        new_matrix = BlockRealMatrix(self.rows, self.columns)
        new_matrix.blocks = [[x * scalar for x in row] for block in self.blocks for row in block]

        return new_matrix

# Example usage
rows, columns = 104, 104  
matrix = BlockRealMatrix(rows, columns)
scalar = 5
result_matrix = matrix.scalar_multiply(scalar)

print("First block of original matrix:")
for row in matrix.blocks[0]:
    print(row)

print("\nFirst block of scaled matrix:")
for row in result_matrix.blocks[0]:
    print(row)
