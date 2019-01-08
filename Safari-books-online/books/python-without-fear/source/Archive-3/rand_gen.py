from time import time

def gen_rand():
     p1 = 1200556037           # Prime number 1
     p2 = 2444555677           # Prime number 2
     max_rand = 2 ** 32
     r = int(time() * 1000)
     while True:
          n = r
          n *= p2
          n %= p1
          n += r
          n *= p2
          n %= p1
          n %= max_rand
          r = n
          yield n

my_gen = gen_rand()
for i in range(10):
    print(next(my_gen) % 100)   # Roll 100-sided die.
