class Matrix2D:
    ''' General-purpose 2-d Matrix class for Life.'''

    def __init__(self, rows, cols):
        ''' Init matrix to rows times cols. '''
        self.grid = [[0] * cols for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_cell(self, r, c):
        ''' Get value at cell r, c. '''
        return self.grid[r][c]

    def set_cells(self, n, *args):
        ''' Set any number of cells to n. '''
        for r, c in args:
            self.grid[r][c] = n

    def inc_cells(self, *args):
        ''' Increment any number of cells by 1 each. '''
        for r, c in args:
            self.grid[r][c] += 1

    def set_all_cells(self, n=0):
        ''' Set any number of cells to n, default 0. '''
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = n

               

    



     
