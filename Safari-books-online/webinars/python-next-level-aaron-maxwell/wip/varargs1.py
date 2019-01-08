def print_args(*args):
  for arg in args:
    print(arg)

print_args(1,2,3,4,5,6,7)

print_args(a=4, b=3) # causes TypeError

def print_kwargs(**kwargs):
  for key, value in kwargs.items():
    print('{}:{}'.format(key, value))

def print_all(*args, **kwargs):
  for arg in args:  # tuple
    print(arg)
  for key, value in kwargs.items(): # dictionary
    print('{}:{}'.format(key, value))