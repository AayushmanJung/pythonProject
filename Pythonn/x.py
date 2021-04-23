#WAP to find factorial of a number by using function.

def factorial(a):
    factorial=1
    num=int(input("Enter the number for factorial: "))
    for i in range(num,0, -1):
        factorial = factorial * i
    return factorial

x = factorial(5)
print(f"The factorial of given number is {x}")