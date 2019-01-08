def main():
    amt = 0
    while True:
        x = get_num()
        if x is None:
            break
        amt += x
    print('The total is', amt)

def get_num(num = 0.0):
    s = input('Input number (ENTER to quit): ')
    if not s:
        return None
    else:
        return float(s)

main()




    

    
    


