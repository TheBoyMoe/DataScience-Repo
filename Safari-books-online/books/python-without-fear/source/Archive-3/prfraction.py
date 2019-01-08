from fractions import Fraction

class PFraction (Fraction):
     def __str__(self):
          n = self.numerator
          d = self.denominator
          i = n // d
          int_str = str(i) + ' ' if i > 0 else ''
          n = n % d
          n_str = str(n) + '/' + str(d) if n > 0 else ''
          return int_str + n_str
     
     def __add__(self, other):
         f = Fraction.__add__(self, other)
         return PFraction(f)

f1 = PFraction('1/2')
f2 = PFraction('2/3')
print('The result is', f1 + f2)
