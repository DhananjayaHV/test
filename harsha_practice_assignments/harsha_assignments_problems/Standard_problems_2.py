class A:
    user_size=int(input("Enter the range :"))

    def __init__(self):
        self.size=A.user_size

    def parenthesis_append(self, result,open=0, close=0):
        if (close == self.size):
            #  When get the result of parentheses in given size
            print(result)
            return

        if (open < self.size):
            #  Add open parentheses
            self.parenthesis_append(result + "(",
                                 open + 1, close)

        if (open > close):
            #  Add close parentheses
            self.parenthesis_append(result + ")",
                                 open, close + 1)


a=A()
a.parenthesis_append("")
