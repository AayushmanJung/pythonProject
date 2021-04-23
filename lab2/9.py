'''
Check whether the given year is leap year or not. If year is leap print 'LEAP YEAR' else print 'COMMON YEAR'.
Hint:
-A year is leap year if its number is exactly divisible by 4 and is not exactly divisible by 100.
-A year is always a leap year if its number is exactly divisible by 400.
'''
input_year=int(input("Enter the year number: "))
if (input_year%400==0) or (input_year%4==0) or (input_year%100==0):
    print("The year is a leap year")
else:
    print("The year  is a common year")