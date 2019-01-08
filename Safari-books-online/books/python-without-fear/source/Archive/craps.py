from random import randint

def main():
    s = ''
    while not s or s[0] in 'Yy':
        play_the_game()
        s = input('Play again? (Y or N): ')

def play_the_game():
    r = roll()
    if r == 7 or r == 11:
        print(r, 'is an instant WINNER!\n')
        return
    if r == 2 or r == 3 or r == 12:
        print(r, 'is an instant LOSER. Sorry.\n')
        return
    print('Your point is now a', r)
    point = r
    while True:
        s = input('Roll again (E = exit)?')
        if len(s) > 0 and s[0] in 'Ee':
            return
        r = roll()
        print('You rolled a', r)
        if r == point:
            print('You\'re a WINNER!\n')
            return
        elif r == 7:
            print('Sorry, you\'re a LOSER.\n')
            return

def roll():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(d1, d2)
    return d1 + d2

main()





    

    
    


