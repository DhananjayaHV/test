str1='my name is The show man'

print(str1[-2:]*4)


def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises'))
