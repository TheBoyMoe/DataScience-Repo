# From Example 8.1: converst to all upper.

input_str = input('Enter input string: ')
my_str = input_str.upper()
a_list = [ch for ch in my_str if ch.isalpha()]
s = ''.join(a_list)

# This part is NEW. Tests for matching letters.

is_palin = True
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        is_palin = False

if is_palin:
    print('String is a palindrome.')
else:
    print('String is NOT a palindrome.')

    


    

    
    


