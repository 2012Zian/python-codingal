def add (p,q):
    return p+q

def subtraction (p,q):
    return p-q

def times (p,q):
    return p*q

def divide (p,q):
    return p/q

print("please select an operation: ")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplycation")
print("D. Divition")

choice = input("please enter option a/b/c/d: ")

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

if choice == "a":
    print(num1, "+" ,num2, "=" ,add(num1,num2))

elif choice == "b":
    print(num1, "-" ,num2, "=" ,subtraction(num1,num2))

elif choice == "c":
    print(num1, "*" ,num2, "=" ,times(num1,num2))

elif choice == "d":
    print(num1, "/" ,num2, "=" ,divide(num1,num2))
else:
    print("invalid input!")