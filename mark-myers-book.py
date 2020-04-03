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
