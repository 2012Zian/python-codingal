try:
    number = int(input("enter a number"))
    print("the number was", number)

except ValueError as e:
    print("the exc is", e)