class A:
  def __init__(self):
    self.stng = input("Enter the string : ")

  def myfunc(self):
      for name in self.stng.split(" "):
          if len(name)%4==0:
            rev=name[::-1]
            print(rev)
            print("Length of the string : ",len(name))
          else:
              pass


p1 = A()
p1.myfunc()