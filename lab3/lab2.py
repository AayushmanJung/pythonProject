'''
Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return "Fizz"
If it is divisible by 5, it should return "Buzz"
If it is divisible by both 3 and 5, it should return "FizzBuzz"
Oherwise, it should return the same number
'''
def fizzbuzz(anynumber):
    if (anynumber%3==0) and (anynumber%5==0):
        return "fizzbuzz"
    elif anynumber%5==0:
        return "buzz"15
    elif anynumber%3==0:
        return "fizz"

user_input=int(input("Enter any number: "))
print(fizzbuzz(user_input))
