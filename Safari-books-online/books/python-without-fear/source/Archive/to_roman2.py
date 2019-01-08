rom_list = [ ('M', 1000), ('CM', 900), ('D', 500),
  ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
  ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
  ('IV', 4), ('I', 1) ]

amt = 0
def make_roman(letter, n):
    global amt
    while amt >= n:
        amt = amt - n
        print(letter, end='')

def main():
    global amt
    amt = int(input('Enter a number: '))
    print('The Roman number is: ', end='')
    for item in rom_list:
        make_roman(item[0], item[1])

main()    
