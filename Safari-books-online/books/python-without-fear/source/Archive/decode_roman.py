rom_list = [ ('M', 1000), ('CM', 900), ('D', 500),
  ('CD', 400), ('C', 100), ('XC', 90), ('L', 50),
  ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
  ('IV', 4), ('I', 1) ]

amt = 0
romstr = ''

def main():
    global romstr
    romstr = input('Enter Roman numeral: ')
    for item in rom_list:
        decode_roman(item[0], item[1])
    print('The equivalent number is', amt)
    
def decode_roman(letters, n):
    global amt, romstr
    sz = len(letters)
    while romstr.startswith(letters):
        amt += n
        romstr = romstr[sz:]

main()    
