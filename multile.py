try:
    num1, num2 = eval(input("Enter 2 numbers seperate by a comma:"))
    result = num1 / num2
    print("Result is " , result)
except  ZeroDivisionError:
    print("Divivsion by zero is error!!")
except  SyntaxError:
    print("Comma is missing.  Enter numbers seperated by comma like this 1,2!")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")






 

