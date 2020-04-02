ef raises_value_error():
  raise ValueError

try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")

def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")
