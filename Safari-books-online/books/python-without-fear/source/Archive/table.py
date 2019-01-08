fib_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
format_str = '{:>2}. {:>4}'
for i, item in enumerate(fib_list, 1):
    print(format_str.format(i, item))

    
    


