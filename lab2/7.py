'''
Given a positive real number, print its fractional part.
'''
import math
user_input=int(input("Enter a number: "))
fractional_number=math.modf(user_input)
print(fractional_number)