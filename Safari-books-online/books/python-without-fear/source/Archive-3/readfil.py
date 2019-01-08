in_file = None

def main():
    if open_file():
        fss = '{:>2}. {}'
        str_list = in_file.readlines()
        for i, item in enumerate(str_list, 1):
            print(fss.format(i, item), end='')
        in_file.close()

# Open file function: return True if file is found...
# Return false if user wants to quite early.

def open_file():
    global in_file
    while True:
        try:
            fname = input('Enter file name: ')
            if not fname:
                return False
            in_file = open(fname)    # Atempt file open.
            return True
        except FileNotFoundError:
            print('File not found. Re-enter.')

main()
