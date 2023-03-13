import math


def garis():
    print('-----------------------')

'''
#konstanta
varPi = math.pi
varE = math.e

print(varPi)
print(varE)

garis()
#faktorial

for i in range(1, 11):
    print (i, math.factorial(i))

garis()
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)
test_var_args('yasoob', 'python', 'eggs', 'test')
'''
garis()
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#some_list = ['a']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print('huruf =', duplicates)
