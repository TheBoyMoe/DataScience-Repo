# Import from the file lifemat.py in the same directory.
from lifemat import Matrix2D

rows = 20
cols = 40
life_mat = Matrix2D(rows, cols)
life_mat.set_cells(1, (1,1), (2,2), (3,0), (3,1), (3,2))
border_str = '_' * cols    # Create border string.

def do_generation():
     print(border_str + '\n' + get_mat_str(life_mat))

def get_mat_str(a_mat):
     disp_str = ''
     for i in range(rows):
          lst = [get_chr(a_mat,i,j) for j in range(cols)]
          disp_str += ''.join(lst) + '\n'
     return disp_str

def get_chr(a_mat, r, c):
     return 'X' if a_mat.get_cell(r, c) > 0 else ' '

do_generation()



     
