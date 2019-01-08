n = 20      # Print primes from 2 up to 20.
comp_list =  [j for i in range(2, n)
                for j in range(i * i, n, i)]
prime_list = [i for i in range(2, n)
                if i not in comp_list]
print(prime_list)


    

    
    


