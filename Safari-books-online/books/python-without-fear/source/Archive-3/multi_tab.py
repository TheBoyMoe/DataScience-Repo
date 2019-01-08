def main():
    rows = cols = 8
    mat = [[(i + 1) * (j + 1) for j in range(cols)]
                              for i in range(rows)]
    # Print out matrix

    
    for i in range(rows):
        for j in range(cols):
            print('{:>2} '.format(mat[i][j]), end='')
        print()

main()
