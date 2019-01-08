bool_list = [True] * 100
for prime in range(2, 100):
    if bool_list[prime]:
        print(prime, end='  ')
        for i in range(prime * 2, 100, prime):
            bool_list[i] = False
    


