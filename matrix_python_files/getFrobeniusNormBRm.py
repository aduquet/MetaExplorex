import math

class BlockMatrix:
    def __init__(self, blocks):
        self.blocks = blocks  

    def get_frobenius_norm(self):
        sum_squares = 0.0
        for block in self.blocks:
            for element in block:
                sum_squares += element * element  

        return math.sqrt(sum_squares)  

# Example usage
blocks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

matrix = BlockMatrix(blocks)
norm = matrix.get_frobenius_norm()
print("Frobenius Norm:", norm)
