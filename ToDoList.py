#from ToDoListWithMenu import get_valid_integer
#from ToDoListWithMenu import Task
import ToDoListWithMenu

print("This is processed in main")
tasks = []

# Main program
while True:
    ToDoListWithMenu.show_menu()
    menu_choice = input("Enter your choice (1-3): ")
    #add a new task
    if menu_choice == "1":
        task = ToDoListWithMenu.Task()
        tasks.append(task)
        print("\nTask Entered Succesfully! \n")
    #get a message
    elif menu_choice == "2":
        print("\nYou are beautiful \n")
    #quit
    elif menu_choice == "3":
        print("Quitting...")
        break
    #if invalid input
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")




#show results before and after completion
print("\nShow results: ")
for task in tasks:
      print(task)
      print()
print()
print("FIXME: Show the task being completed: ")
for task in tasks:
      task.mark_as_completed()
      print(task)
      print()








