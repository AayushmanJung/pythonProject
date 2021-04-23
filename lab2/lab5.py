'''
If name is less than 3 characters
long - name must be at least
3 characters
otherwise if it's more than
50 characters - name must be maximum of 50 characters
otherwise - name looks good!
'''

user_name=input("Enter your good name")
length_username=len(user_name)
if (length_username<=3):
    print("Your name is not valid")
elif (length_username>=50):
    print("it also cannot be valid")
elif (length_busername>3) and (length_username<50):
    print("your name is valid")