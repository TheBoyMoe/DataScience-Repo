n = int(input('Enter number to calc. factorial for: '))
prod = 1
for i in range(1, n + 1):   # For 1 to n inclusive,
    prod = prod * i
s = str(prod)               # Convert factorial to string s
z = len(s) - len(s.strip('0'))
print('n factorial is', s)
print('The number of trailing zeros is', z)
      



    

    
    


