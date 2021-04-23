'''
If temperature is greater than 30,
it's a hot day other wise if
it's less than 10;
it's a cold day; otherwise,
it's neither hot nor cold.
'''

user_temperature=int(input("Enter temperature of the day: "))
if user_temperature >30:
    print("Its a hot day")
elif (user_temperature<10):
    print("Its a cold day")
else:
    print("Its neither hot nor cold")




