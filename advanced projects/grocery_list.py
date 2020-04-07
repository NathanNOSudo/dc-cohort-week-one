shoppingList = []
items =[]
user_input =""
option = print(input("\n   ______________________________ \n / \                             \. \n|   |                            |. \n \_ |                            |. \n    |                            |. \n    |       ** Grocery  **       |. \n    |            List            |. \n    |                            |. \n    |   Press 1 to make list    |. \n    |  Press 2 to add a item  |. \n    |    Press 3 to view list    |. \n    |      Press q to quit       |. \n    |                            |. \n    |                            |. \n    |                            |. \n    |   _________________________|___ \n    |  / By: Nathan NOSudo          /. \n    \_/____________________________/. \n \n>>>>>>>"))

def help_instruc():
    print(option)
    if option == "1":
        return input("Please enter the name of the store: ")
        return input("please enter your item to add:")
    if option == 2:
        print(input("enter the number corresponding to the item you wish to delete: "))

while option != "q":
  print("REMEMBER TO SANITIZE YOUR HANDS!")
  break
#User inputs 1 to add items
  if option == "1":
    item = input("Please input your Item: ")
#    store =
    priority = input("Defcon3, Defcon2, or Defcon1 priority: ")

    item = {
      "item": item,
      "priority": priority
    }
    print("-------------------------------------------------------")
    print("Thank You! {} has been to your grocery list! your list now contains {} items".format(item, len(shoppingList)))

    print("DO NOT FORGET TO SANITIZE")    
#User inputs 2 to delete items
  elif option == "2":
    for index in range(0, len(items)):
      itemsdict = items[index]
      itemtitle = item_dict[item]
      itemstore = item_stores[store]
      item_priority = item_dict[priority]
      print(f"{index+1}  {item_title} {item_store} {item_priority}")
      
    item_to_delete = int(input("I hope its completed....no take backs! Input number corresponding to item to you wish to delete: "))

#def shopping_list():
    print("---------------")
    print("Grocery List:")
    print("---------------")
    for item in shoppingList:
        print("> " + item)
        
def add_item_to_list(item):
    shoppingList.append(item)
    print("-------------------------------------------------------")
    print("Thank You! {} has been to your grocery list! your list now contains {} items".format(item, len(shoppingList)))

#name = input("Please enter the name of the store: ")
#item = input("Please enter the item you want to add to your list... ").upper()       
help_instruc()
def main():
#    help_instruc()
    name = input("Please enter the name of the store: ")
    item = input("Please enter the item you want to add to your list... ").upper()          
    while user_input != "q":
        name = input("Please enter the name of the store: ")
        item = input("Please enter the item you want to add to your list... ").upper()
        if item == 1:
            shopping_list()
        elif item == "view":
            shopping_list()
        elif item == "help":
           help_instruc()
        else: 
           add_item_to_list(item)

help_instruc()            
main()
