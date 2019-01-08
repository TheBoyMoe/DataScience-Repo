from time import time

def diagnostics(f):
    def wrapper(*args, **kywrds):
        print('Executed', f.__name__, 'at', time())
        value = f(*args, **kywrds)
        print('Exited  ', f.__name__, 'at', time())
        print('Arguments:', args)
        print('Keyword args:', kywrds)
        print('Value returned:', value, '\n')
        return value
    return wrapper

@diagnostics
def print_nums():
     for i in range(4):
         print(i, end='\t')
     print()

@diagnostics
def calc_hypotenuse(a, b):
    return ((a*a + b*b) ** 0.5)  # Return sqrt of c * c

print_nums()
print (calc_hypotenuse(a = 3, b = 4))
