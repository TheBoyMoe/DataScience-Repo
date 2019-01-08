n = 5
mat1 = [[0] * n for i in range(n)]

def main():
    enter_mat_vals()
    print_mat()
    s = ''
    while not s or s[0] not in 'Nn':
        rotate_mat()
        print('Here is the rotated version:')
        print_mat()
        s = input('Rotate matrix again? (Y or N): ')

def rotate_mat():
    global mat1
    mat2 = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            mat2[j][n - 1 - i] = mat1[i][j]
    mat1 = mat2

def enter_mat_vals():
    for i in range(n):
        s = input('Enter a row of values: ')
        a_list = s.split()
        for j, item in enumerate(a_list[:n]):
            mat1[i][j] = int(item)

def print_mat():
    s = ''
    for i in range(n):
        for j in range(n):
            s += '{:>3} '.format(mat1[i][j])
        s += '\n'
    print(s)

main()
