#Function having no parameter and no return type.
def add():
    a=6
    b=6
    print(a+b)
add()

#Function having parameter and no return type.
def sub(a,b):
    print(a-b)
sub(6,4)

#Function having no parameter and with return type.
def mul():
    a=10
    b=2
    return a*b
product = mul()
print(product)

#Function having parameter and with return type

def div(a,b):
    return a/b
divide = div(20,2)
print(divide)