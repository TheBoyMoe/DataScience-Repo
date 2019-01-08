prod = 1
for i in range(1, 51):      # For 1 to 50 inclusive,
    prod = prod * i
s = str(prod)               # Convert factorial to string s
n = len(s)                  # n = length of string s
z = 0
while n > 0 and s[n - 1] == '0':
    z = z + 1
    n = n - 1
print('50! is', s)
print('The number of trailing zeros is', z)
      



    

    
    


