# print(0.1+0.2==0.3)


# #python int demo

# number = 10 ** 1000
# print("Number created succesfully")
# print("Digits:, len(str(number))")
# print(number)


# a = 10
# b = 3.14

# print(type(a))
# print(type(b))


# hours, mins = divmod(135,60)
# print(hours, mins)

#PEDAS
#print(2+3*4**2)

# name = input("Enter your name: ")
# print(name)
# job = input("What you do bro? ")
# print("I am a",job)


# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# res = a + b
# print(f"Sum of {a} and {b} is {res}")

# a = float(input("Enter number : "))
# print(f"{a},{type(a)}")

# radius = float(input("Enter radius of circle: "))
# area = 3.14 * (radius*radius)
# print(f"area of circle is {area},{type(area)}")

# celsius = int(input("Enter Celsius: "))
# Fahrehnheit = celsius * 9/5 + 32
# print()


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number"))
operator = input("Enter operator(+,-,*,/,%): ")

if operator == "+":
    print("Result: ",num1 + num2)
elif operator == "-":
    print("Result: ",num1 - num2)
elif operator == "*":
    print("Result: ",num1 * num2)
elif operator == "%":
    print("Result: ",num1 % num2)
elif operator == "%":
    print("Result: ",num1 % num2)
else:
    print("operator is not valid")


