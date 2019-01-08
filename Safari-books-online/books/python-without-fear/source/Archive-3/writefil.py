def main():
    out_file = open('stuff.txt', 'w')
    while True:
        s = input('Enter>>')
        if not s:
            break
        out_file.write(s + '\n')
    out_file.close()
    print('Done!')

main()
