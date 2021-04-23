'''
car game:
>help
start - to start car
stop - to stop the car
quit - to exit
>asd
I don't understand this
>start
car started... Ready to go!!!
>stop
car stopped...
>quit
'''
command_repeat=0
first_command='start'
second_command='stop'
third_command='quit'

while command_repeat<=2:
    command_repeat+=1
    user_command=input("Enter any command")
    if user_command==first_command:
        print("car started...Ready to go!!!")
    elif user_command==second_command:
        print("Car stopped...")
    elif user_command==third_command:
        print("Quit")
    else:
        print("I don't understand")