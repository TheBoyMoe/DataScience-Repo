class Point3D:
     '''Three dimensional point class, supporting
        subtraction and comparison. '''

     def __init__(self, x, y, z):
          self.x = x
          self.y = y
          self.z = z

     def __sub__(self, other):
          d1 = self.x - other.x
          d2 = self.y - other.y
          d3 = self.z - other.z
          return Point3D(d1, d2, d3)

     def __eq__(self, other):
          return(self.x == other.x and self.y == other.y
                 and self.z == other.z)

def main():
     s = ''
     while not s or s[0] in 'Yy':
          p1 = get_point()
          p2 = get_point()
          p3 = get_point()
          if is_win(p1, p2, p3):
               print('Is a winning combination.')
          else:
               print('Is not a win.')
          s = input('Do again (Y or N)?')

def get_point():
     s = input('Enter point in x, y, z format: ')
     ls = s.split(',')
     x, y, z = int(ls[0]), int(ls[1]), int(ls[2])
     return Point3D(x, y, z)

def is_win(p1, p2, p3):
     if (p3 - p2 == p2 - p1
      or p2 - p3 == p3 - p1
      or p3 - p1 == p1 - p2):
          return True
     else:
          return False

main()
     
