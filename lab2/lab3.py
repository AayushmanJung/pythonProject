'''
Price of a house is $1M .
If a buyer has good credit, they need to put down 10% otherwise they need to put down 20%.
Print down the payment.
'''
price_of_house=1000000
down_payment=input("choose if you have good credit or not?\n")
if(down_payment=="good credit"):
    print(f"the amount after good credit={int(10/100*1000000)}")
else:
    print(f"the amount when you have not any good credit is {int(20//100*1000000)}")