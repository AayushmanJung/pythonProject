'''
WAP to find A.M. or P.M. from the tim given by user given by the user.
'''

user_time = int(input("Enter the time: "))
if (user_time >= 1 and user_time <= 12):
    print('The time is A.M.')
else:
    print('The time is P.M.')



