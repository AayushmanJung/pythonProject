'''
weight converter:
input the weight of person in either kg or lbs.
if the person provides his/her wight in kg then convert to lbs
else convert it into kg.
'''
user_weight=float(input("please enter your weight:\n" ))
user_choice=input("choose if you want to convert it to kg or pounds\n")
if user_choice=="kg":
    print(f"The weight in pounds is {user_weight*0.45359237}")
elif (user_choice=="pounds"):
    print(f"The weight in kg is {user_weight*2.20462262}")
else:
    print("Not recognized. Pick between kg and pounds.")
