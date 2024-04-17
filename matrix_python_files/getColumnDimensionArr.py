class RealMatrix:
    def __init__(self, data):
        self.data = data

    def getColumnDimension(self):
        if self.data is None or not self.data:  
            return 0  
        elif self.data[0] is None:  
          return 0
        else:  
            return len(self.data[0]) 

matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = RealMatrix(matrix_data)
print(matrix.getColumnDimension())  