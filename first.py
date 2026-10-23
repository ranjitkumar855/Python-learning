#WAP to display the sum of 10 and 20
# a = 10
# b = 40
# print("Sum of two number is",a+b)


x = 10
print(x,type(x))

x = "Ranjit Kumar"
print(x,type(x))

x = True
print(x,type(x))

import dis

def add(a, b):
    return a + b

dis.dis(add)