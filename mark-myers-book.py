#elimnates sink from list using index number. prints whats left.
products = ["lamp", "table", "chair", "couch", "sink"]
del products[4]
print(products)

#removes sink using its value. prints remaining items.
products = ["lamp", "table", "chair", "couch", "sink"]
products.remove("sink")
print(products)

#loop through a list, displaying each element.
for x in y:
  print(x)

#loop with comparing if equal to a value
for x in y:
  if x == z:
    print("ok")

#for loop another example checking if an elements has the same valuew as variable my_street
my_street = "Main"
streets = ("Elm", "Walnut", "Center", "Main", "Front")
for a_street in streets:
  if a_street == my_street:
    print("yes")

#list with 3 elements. loop through and display each element.
cars = ["Tesla", "Bolt", "Leaf"]
for a_car in cars:
  print(a_car)

#for loops nested

""" The second, or inner, loop runs a complete cycle of iterations on each iteration of the first, or outer, loop. The outer loop begins with the first name, BlueRay. The inner loop then runs four iterations, combining BlueRay with each of the four last names—Zzz, Burp, etc. It appends each combination to the list full_names. When that's finished, the program returns to the outer loop, which moves to the next first name, Upchuck. Then it jumps to the inner loop, which combines this name with each of the four last names and appends these combinations to the list full_names. It keeps going like this until all 20 combinations have been added to the list of full names. """

first_names = ["BlueRay ", "Upchuck ", "Lojack ", "Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []
for a_first_name in first_names:
  for a_last_name in last_names:
    full_names.append(a_first_name + " " + a_last_name)

