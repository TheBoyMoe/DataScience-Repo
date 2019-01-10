class Person:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def full_name(self):
    return '{} {}'.format(self.first, self.last)

  def formal_name(self, title):
    return '{} {}'.format(title, self.full_name())


p = Person('Tom', 'Jones')
print(p.formal_name('Mr.'))
print(p.full_name())