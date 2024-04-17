class Matrix:
    def __init__(self, data):
        self.data = data

    def get_row_dimension(self):
        return len(self.data)

    def get_column_dimension(self):
        return len(self.data[0]) if self.data else 0

    def get_entry(self, row, col):
        return self.data[row][col]

    def get_data(self):
        rows = self.get_row_dimension()
        columns = self.get_column_dimension()

        new_data = [[0] * columns for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                new_data[i][j] = self.get_entry(i, j)

        return new_data