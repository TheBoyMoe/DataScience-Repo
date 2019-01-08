class Temperature:
    ''' This class is a Temperature object that stores
just one value, but represented two different ways.'''
    
    def __init__(self, tmp=32.0):
        self.tmp = tmp

    @property
    def cels(self):
        return (self.tmp - 32.0) / 1.8

    @cels.setter
    def cels(self, new_t):
        self.tmp = new_t * 1.8 + 32.0

my_tmp = Temperature()
my_tmp.cels = 0
print('0 C. is', my_tmp.tmp, 'F.')
my_tmp.cels = 100
print('100 C. is', my_tmp.tmp, 'F.')
my_tmp.cels = 50
print('50 C. is', my_tmp.tmp, 'F.')
my_tmp.tmp = 86
print('86 F. is', my_tmp.cels, 'C.')
