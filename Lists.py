#TODO: fix 'invalid input' block when attempting to remove from empty array
#TODO: user should not be able to input empty items

toDo = []
completed = []
def mainMenu():
    global menuInput
    menuInput = input("Available commands: \n1. Add task \n2. Remove task \n3. Remove completed task \n4. View to-do list \n5. View completed tasks \n")
    while not (menuInput == "1" or menuInput == "2" or menuInput == "3" or menuInput == "4" or menuInput == "5"):
        print("Invalid input.")
        menuInput = input("Available commands: 1. Add task, 2. Remove task, 3. View to-do list, 4. View completed tasks. \n")
    if menuInput == '1':
        task = input("Enter the task you wish to add. \n")
        toDo.append(task)
        mainMenu()
    if menuInput == '2':
        remTask = input("Enter the task you wish to remove. \n")
        while True:
            if remTask in toDo:
                break
            else:
                print("Invalid input.")
                remTask = input("Enter the task you wish to remove. \n")
        toDo.remove(remTask)
        mainMenu()
    if menuInput == '3':
        remComTask = input("Enter the task you wish to remove. \n")
        while True:
            if remComTask in toDo:
                break
            else:
                print("Invalid input.")
                remComTask = input("Enter the task you wish to remove. \n")
        completed.append(remComTask)
        toDo.remove(remComTask)
        mainMenu()
    if menuInput == '4':
        print("\n \nTo-do list:")
        for i in toDo:
            print(i+"\n")
        mainMenu()
    if menuInput == '5':
        print("\n \nCompleted tasks:")
        for i in completed:
            print(i+"\n")
        mainMenu()
mainMenu()
    
