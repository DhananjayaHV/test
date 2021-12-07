'''Remove spaces from dictionary keys. '''
Product_list = {'P 01': 'DBMS', 'P 02': 'OS',
                'P 0 3 ': 'Soft Computing'}
class A:

    def __init__(self,dictn):
        self.dctny = dictn

    def Sort_list(self):
        Product_list = {x.replace(' ', ''): v for x, v in self.dctny.items()}
        print(" New dictionary : ", Product_list)



a=A(Product_list)
a.Sort_list()