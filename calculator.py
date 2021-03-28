import math


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def pow(x,y):
    return x**y
def logarithm(x):
    return math.log(x)
def log2(x):
    return math.log2(x)
def squreroot(x):
    return math.sqrt(x)
def cosine(x):
    return math.cos(x)
def sine(x):
    return math.sin(x)
def tangent(x):
    return math.tan(x)
def radian(x):
    return math.radian(x)


print("Select operation.")
print("1.add")
print("2.Sub")
print("3.Mul")
print("4.Div")
print("5.pow")
print("6.logarithm")
print("7.log2")
print("8.squareroot")
print("9.cosine")
print("10.sine")
print("11.tangent")
print("12.radian")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6','7','8','9','10','11','12'):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print(a, "+", b, "=", add(a,b))
        elif choice == '2':
            print(a, "-", b, "=", sub(a,b))
        elif choice == '3':
            print(a, "*", b, "=", mul(a,b))
        elif choice == '4':
            print(a, "/", b, "=", Div(a,b))
        elif choice == '5':
            print(num1, "pow", num2, "=", divide(a,b))
        elif choice == '6':
            print(a, "logarithm", "is" "=", logarithm(a))
        elif choice == '7':
            print(a, "log2", "is" "=", log2(a))
        elif choice == '8':
            print(a, "squareroot", "is" "=",squreroot(a))
        elif choice == '9':
            print(a, "cosine", "is" "=", cosine(a))
        elif choice == '10':
            print(a, "sine", "is" "=", sine(a))
        elif choice == '11':
            print(a, "tangent", "is" "=", tangent(a))
        elif choice == '12':
            print(a, "radian", "is" "=", radian(a))
        break
    else:
        print("Invalid Input")
Output
