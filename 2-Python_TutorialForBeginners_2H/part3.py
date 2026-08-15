# Arithmatic operators
# Comparison operators
# Logical Operators

# if else condition (Conditioanl statements)


# age = 24

# if age >= 18:
#     print("You are an adult")
# elif age < 18 and age >= 13:
#     print("You are a teenager")
# else: 
#     print("You are not an adult")


# marks = int(input("Enter your marks: "))

# if marks >= 80:
#     print("A")
# elif marks < 80 and marks >= 60:
#     print("B")
# elif marks < 60 and marks >= 40:
#     print("C")
# else: 
#     print("D")

# Calculator
a = float(input("Enter 1st numb : "))
b = float(input("Enter 2nd numb : "))
op = input("Enter Operator(+,-,*,/,%,**): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '%':
    print(a % b)
elif op == '**':
    print(a ** b)
else:
    print("Invalid operator")
