class A:
  def __init__(self, name):
    self.name = name

  def myfunc(self):
    rev=self.name[::-1]
    print(rev)


p1 = A("Python")
p1.myfunc()