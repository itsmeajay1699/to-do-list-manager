
class Task:
    
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        return f"{self.title} - {self.description} - {self.completed}"
    
    def completeTask(self):
        self.completed = True
    
    def uncompleteTask(self):
        self.completed = False


class ToDoList:
    tasks = []
    def addTask(self,title,description):
        task = Task(title,description)
        self.tasks.append(task)
    def removeTask(self,task1):
        for task in self.tasks:
            if task.title == task1.title and task.description == task1.description:
                self.tasks.remove(task)
    def taskCompleted(self,checkNumber):
        self.tasks[checkNumber].completeTask()
    
    def taskUncompleted(self,checkNumber):
        self.tasks[checkNumber-1].uncompleteTask()
    
    def showTasks(self):
        return self.tasks

while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. Complete task")
    print("4. Uncomplete task")
    print("5. Show tasks")
    print("6. Exit")
    option = int(input("Select an option: "))
    if option == 1:
        title = input("Enter title: ")
        description = input("Enter description: ")
        ToDoList().addTask(title,description)
    elif option == 2:
        title = input("Enter title: ")
        description = input("Enter description: ")
        ToDoList().removeTask(Task(title,description))
    elif option == 3:
        for i,task in enumerate(ToDoList().showTasks()):
            print(i+1,task)
        checkNumber = int(input("Enter the number of the task you want to complete: "))
        ToDoList().taskCompleted(checkNumber)
    
    elif option == 4:
        checkNumber = int(input("Enter the number of the task you want to uncomplete: "))
        ToDoList().taskUncompleted(checkNumber)
    elif option == 5:
        for i,task in enumerate(ToDoList().showTasks()):
            print(i+1,task)
    elif option == 6:
        break
    else:
        print("Invalid option")


           


        