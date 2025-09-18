def add (P , Q):
    return P + Q

def subtract (P , Q):
    return P - Q

def multipy (P , Q):
    return P * Q

def dvide (P , Q):
    return P / Q


print("Please select the operation")
print("a.ADD")
print("b.SUB")
print("c.MUL")
print("d.DIV")
choice = input("Please enter your choice(a/b/c/d)")
num1= int(input("Please enter the first number"))
num2= int(input("Please enter the second number"))

if choice == 'a':
    print(num_1, "+" , num_2, "=" , add(num_1,num_2))
elif choice == 'b':
    print(num_1, "-" , num_2, "=" , subtract(num_1,num_2))

elif choice == 'c':
    print(num_1, "*" , num_2, "=" , multiply(num_1,num_2))

elif choice == 'd':
    print(num_1, "/" , num_2, "=" , divide(num_1,num_2))
elif 





