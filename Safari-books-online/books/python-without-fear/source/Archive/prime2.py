bool_list = [True] * 100
primes_found_list = []
for prime in range(2, 100):
    if bool_list[prime]:
        primes_found_list.append(str(prime))
        for i in range(prime * prime, 100, prime):
            bool_list[i] = False
out_str = '  '.join(primes_found_list)
print(out_str)

    


