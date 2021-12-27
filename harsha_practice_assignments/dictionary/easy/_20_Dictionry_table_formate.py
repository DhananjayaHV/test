# Define the dictionary
# dict = {}

# Insert data into dictionary
dict1 = {1: ["Samuel", 21, 'Data Structures'],
         2: ["Richie", 20, 'Machine Learning'],
         3: ["Lauren", 21, 'OOPS with java'],
         }

class A:

    def __init__(self,dict1):
        self.dic1=dict1

    def dict_table(self):
        # Print the names of the columns.
        print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

        # print each data item.
        for key, value in self.dic1.items():
            name, age, course = value
            print("{:<10} {:<10} {:<10}".format(name, age, course))


a=A(dict1)
a.dict_table()