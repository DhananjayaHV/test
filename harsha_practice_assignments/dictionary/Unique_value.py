''''Print all unique values in a dictionary. '''

dictr = {'511':2,'512':3,'513':3,'514':4,'515':4}

class A:

  def __init__(self):
    pass

  def Unique_values(self,dct1):
    # list1=set(dct1.values())
    lst=[]
    for val in dct1.values():
      if val in lst:
        continue
      else:
        lst.append(val)

    print(lst)

a=A()
a.Unique_values(dictr)