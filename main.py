#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("enter bill amount:\n"))
number_of_participant = int(input("Enter number of people:\n"))
tip = (input("Tip amount:\n"))
tip_vlaue = float((float(tip)/100)+1)

payment_per_person = (bill/number_of_participant)*tip_vlaue
print(format(payment_per_person,".2f"))