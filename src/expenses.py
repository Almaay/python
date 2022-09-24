#Greetings
print("Welcome to Almaay's expenses calculator")

#fetching details 
daily_income = float(input("Enter your daily income:"))
income = daily_income * 30

mine = income * 0.1
emergency = income * 0.2
pocket = income * 0.7

#printing details  
print("Pay yourself:", mine)
print("Keep for emergencies", emergency)
print("You can spend:", pocket)
#calculating details 
def pocket_total(tea = 110, card = 90, spend = 150 ):
  return (tea + card + spend) * 30

#testing func  
expenses = pocket_total()
leftover = pocket - expenses
print("Total expenses:", expenses)
print("You can save as leftover:", leftover)