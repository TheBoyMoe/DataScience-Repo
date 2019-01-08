class PointN:
     '''General-purpose multidimensional point class. '''

     def __init__(self, *args):
          # If first arg is a list...
          if isinstance(args[0], list):
              self.the_list = [i for i in args[0]]

          # Otherwise, process all the args as a list.
          else:
              self.the_list = [i for i in args]
          self.list_len = len(self.the_list)

     def __str__(self):
         al_list = [str(i) for i in self.the_list]
         return 'point(' + ', '.join(al_list) + ')'

     def __add__(self, other):
          ''' Add two points together & return a point.'''
          new_list = []
          n = min(self.list_len, other.list_len)
          for i in range(n):
              new_list.append(self.the_list[i] + other.the_list[i])
          return PointN(new_list)

pt1 = PointN(1, 2, 3, 4)
a_list = [10, 10, 10, 10]
pt2 = PointN(a_list)
print('pt1 is', pt1)
print('pt2 is', pt2)
print('Sum is', pt1 + pt2)

     
