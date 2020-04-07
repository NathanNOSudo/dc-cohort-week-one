option = input("\n   ______________________________ \n / \                             \. \n|   |                            |. \n \_ |                            |. \n    |                            |. \n    |       ** Grocery  **       |. \n    |            List            |. \n    |                            |. \n    |   Press 1 to add a item    |. \n    |  Press 2 to delete a item  |. \n    |    Press 3 to view list    |. \n    |      Press q to quit       |. \n    |                            |. \n    |                            |. \n    |                            |. \n    |   _________________________|___ \n    |  / By: Nathan NOSudo          /. \n    \_/____________________________/. \n \n>>>>>>>")
tasks = []

while option != "q":
  print("REMEMBER TO SANITIZE YOUR HANDS!")
#User inputs 1 to add tasks
  if option == "1":
    title = input("Please input your task: ")
    priority = input("Defcon3, Defcon2, or Defcon1 priority: ")

    task = {
      "title": title,
      "priority": priority
    }
    # add dictionary to tasks[]
    tasks.append(task)
    print("DO NOT FORGET TO SANITIZE")    
#User inputs 2 to delete tasks
  elif option == "2":
    for index in range(0, len(tasks)):
      task_dict = tasks[index]
      task_title = task_dict["title"]
      task_priority = task_dict["priority"]
      print(f"{index+1}  {task_title}  {task_priority}")
      
    task_to_delete = int(input("I hope its completed....no take backs! Input number corresponding to task to you wish to delete: "))

    del tasks[task_to_delete]

#User inputs 3 to view all tasks
  elif option == "3":
    for index in range(0, len(tasks)):
      task_dict = tasks[index]
      task_title = task_dict["title"]
      task_priority = task_dict["priority"]
      print(f"{index+1}  {task_title}  {task_priority}")
      print("I HOPE YOU HAVE BEEN SANITIZING YOUR HANDS!")
#if wrong button is pressed
  #else:
   # print("Please press 1, 2, 3, or q")

  option = input("Press 1 to add tasks; Press 2 to delete tasks; Press 3 to view all tasks; Press q to quit: ")
