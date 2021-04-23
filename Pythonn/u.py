'''
WAP to check a number given by the user is a armstrong number or not.
'''

num=int(input("Enter a number: "))
sum = 0
while num>0:
    rem = num%10
    cube= rem**3
    num = num//10
    sum = sum + cube
if (rem==int(num)):
    print(f,'The number is armstrong.')
else:
    print('The number is not armstrong.')
print(sum)
