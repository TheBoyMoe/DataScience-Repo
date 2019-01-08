def main():
    age = int(input('Enter your age, please: '))
    name_str = input('Enter your name, please: ')
    print('Happy birthday,', name_str, '.', sep='')
    print('You are', age, 'years old.')
    if age > 12 and age < 20:
        print('You are a teenager!')
    else:
        print('You\'re NOT a teenager!')

main()



