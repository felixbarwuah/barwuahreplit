#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#dinheiro=(150/5*1.05)
#dinheiro2=round(dinheiro,2)
#print(f"Everyone has to pay {dinheiro2} dinheiro mothafucka")

print("Welcome to the tip calculator Mothafucka ")
totalbill = input("How much was the total bill? $")
percentage = input("What percentage tip would you like to give? 10%,12%, or 15?% ")
amountpeople = input("How many idiots are there? ")

tb = float(totalbill)
pc = int(percentage)/100+1
ap = int(amountpeople)

calc = (tb/ap)*pc 

dinheiro = round(calc,2)
dinheiro = "{:.2f}".format(calc)

print(f"Everyone has to pay ${dinheiro} dinheiros mothafucka")
