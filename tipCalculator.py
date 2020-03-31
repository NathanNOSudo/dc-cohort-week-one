price_meal = float(input("How much did your meal cost? "))
tip = input('what percentage would you like to tip? ')
conv_tip = float(tip) / 100
total = price_meal * conv_tip
print(total)
