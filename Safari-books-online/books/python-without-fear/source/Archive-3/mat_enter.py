def main():
    rows = cols = 5
    mat = [[0] * cols for i in range(rows)]
    for i in range(rows):
        s = input('Enter a row of values: ')
        a_list = s.split()
        for j, item in enumerate(a_list[:cols]):
            mat[i][j] = int(item)
    print_mat(mat)

# Print_mat function. This is written in such a way
# that size information (row, col) does not need to
# be passed in as extra argument.

def print_mat(mat):
    s = ''
    for a_row in mat:
        for item in a_row:
            s += '{:>3} '.format(item)
        s += '\n'
    print(s)

main()
