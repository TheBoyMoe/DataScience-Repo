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
    make_roman('M', 1000)
    make_roman('CM', 900)
    make_roman('D', 500)
    make_roman('CD', 400)
    make_roman('C', 100)
    make_roman('XC', 90)
    make_roman('L', 50)
    make_roman('XL', 40)
    make_roman('X', 10)
    make_roman('IX', 9)
    make_roman('V', 5)
    make_roman('IV', 4)
    make_roman('I', 1)

main()    
