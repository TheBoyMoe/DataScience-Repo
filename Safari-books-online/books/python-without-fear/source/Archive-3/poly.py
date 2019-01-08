class Polygon:
    pi = 3.14159265

    @ staticmethod
    def get_area(factors, sides, cfacts):
        data = []
        for name in sides:
            x = float(input('Enter ' + name + ': '))
            data.append(x)
        prod = 1
        for i in factors:
            prod *= data[i - 1]
        for i in cfacts:
            prod *= i
        return prod

class Square(Polygon):
    def __init__(self):
        self.a = Polygon.get_area([1,1], ['side'], [])


class Circle(Polygon):
    def __init__(self):
        self.a = Polygon.get_area([1,1], ['radius'], [Polygon.pi])


class Sphere(Polygon):
    def __init__(self):
        self.a = Polygon.get_area([1,1,1], ['radius'], [Polygon.pi, 4/3])


print('The area of a square...')
s1 = Square()
print('The area is the suqare is', s1.a)

print('The area of a circle...')
c1 = Circle()
print('The area if a circle is', c1.a)

print('The volume of a sphere...')
sph = Sphere()
print('The volume of the sphere is', sph.a)

