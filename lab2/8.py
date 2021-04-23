'''
Given a three-digit number. Find the sum of its digits.
'''

user_input=int(input("Enter a three digit number: "))
sum=0
while user_input>0:
    reminder=user_input%10
    sum=sum+reminder
    user_input=user_input//10
print("The sum of the given number is",sum)