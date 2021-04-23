'''
Game finding a secret number within 3 attempts.
'''
num=0
secret_num=6
while num<=2:
    num+=1
    num1=num
    guess=int(input("Enter any number: "))
    if guess==secret_num:
        print("Your guess is correct")
    else:
        print("Your guess is incorrect, please try again")