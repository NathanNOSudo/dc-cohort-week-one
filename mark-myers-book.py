#elimnates sink from list using index number. prints whats left.
products = ["lamp", "table", "chair", "couch", "sink"]
del products[4]
print(products)

#removes sink using its value. prints remaining items.
products = ["lamp", "table", "chair", "couch", "sink"]
products.remove("sink")
print(products)
