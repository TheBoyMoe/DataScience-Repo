# Import from the file lifemat.py in the same directory.
from lifemat import Matrix2D

rows = 20
cols = 40
life_mat = Matrix2D(rows, cols)
nc_mat = Matrix2D(rows, cols)
life_mat.set_cells(1, (1,1), (2,2), (3,0), (3,1), (3,2))
border_str = '_' * cols    # Create border string.

def get_mat_str(a_mat):
     disp_str = ''
     for i in range(rows):
          lst = [get_chr(a_mat,i,j) for j in range(cols)]
          disp_str += ''.join(lst) + '\n'
     return disp_str

def get_chr(a_mat, r, c):
     return 'X' if a_mat.get_cell(r, c) > 0 else ' '

# Do Generation function.
# Print the current state of life_mat, and then process
# one generation.

def do_generation():

    # Pring the current 'Life' state
    print(border_str + '\n' + get_mat_str(life_mat))
    
    nc_mat.set_all_cells(0)

    # Populate nc_mat, but 1) looking at each living
    # cell in life_mat, and for each, increment all
    # surrounding positions... in nc_mat. Use % op
    # to implement "wrap around" at edges & corners.

    for i in range(rows):
        for j in range(cols):
            if life_mat.get_cell(i, j):
                im = (i - 1) % rows
                ip = (i + 1) % rows
                jm = (j - 1) % cols
                jp = (j + 1) % cols

                nc_mat.inc_cells( (im, jm), (im, j),
                    (im, jp), (i, jm), (i, jp), 
                    (ip, jm), (ip, j), (ip, jp) )

    # Process a generation, by comparing neighbor
    # counts to living cells, and applying the 2 rules.

    for i in range(rows):
        for j in range(cols):
            n = nc_mat.get_cell(i, j)
            if n < 2 or n > 3:                # Death.
                life_mat.set_cells(0, (i, j))
            elif n == 3:                      # Birth                
                life_mat.set_cells(1, (i, j))

n = int(input("How many generations of slider? "))
for i in range(n):
    do_generation()




     
