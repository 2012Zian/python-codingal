try:
    num1 ,num2 = eval(input("enter 2 numbers separated by commas"))
    result =  num1/num2
    print("the result is",result)
    

except ZeroDivisionError:
    print("division by zero is error.")

except SyntaxError:
    print("comma is missing,enter numbers like this 4,6")

except:
    print('wrong input')

else:
    print('no exceptions')

finally:
    print("this will execute no matter what")

