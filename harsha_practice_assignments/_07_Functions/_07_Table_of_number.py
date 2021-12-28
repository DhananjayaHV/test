class Table():
    user_input = int(input("Enter the number : "))

    def table_calculatore(self):
        for i in range(1, 11):
            result = Table.user_input * i
            print(f'{Table.user_input} X {i} = {result}')


a=Table()
a.table_calculatore()