def loadFile(file_name):
    with open(file_name, 'r') as f:
        file = f.readlines()
    return [data.strip() for data in file]

def saveFile(file_name, data_list):
    with open(file_name, 'w') as f:
        for data in data_list:
            f.write(data + '\n')

def printTasks(data):
    for i in range(len(data)):
        print(f"{i + 1}. {data[i]}")

def menu():
    while True:
        print("\n --- TO DO List --- \n")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")
        tasks = loadFile('tasks.txt')
        compl = loadFile('tasks_completed.txt')
        files = [tasks, compl]
        while True:
            try:
                m = int(input("Choose your action: "))
                break
            except ValueError:
                print("ERROR: Invalid action")
        print('\n')
        if m == 1:
            print('\n Tasks TO DO: ')
            printTasks(tasks)
            print('\n Tasks Completed: ')
            printTasks(compl)
        elif m == 2:
            task = input("Input your task: ")
            tasks.append(task)
            saveFile('tasks.txt', tasks)
        elif m == 3:
            while True:
                try:
                    t = int(input("Choose file. 1. To Do, 2. Completed: "))
                    break
                except ValueError:
                    print("ERROR: Invalid action")
            if t != 1 and t != 2:
                print("ERROR: Invalid action")
            else:
                if t == 1:
                    printTasks(files[t - 1])
                    while True:
                        try:
                            n = int(input("Enter the number of the task to remove: "))
                            break
                        except ValueError:
                            print("ERROR: Invalid number")
                    if n < 1 or n > len(files[t - 1]):
                        print("Invalid task number")
                    else:
                        del files[t - 1][n - 1]
                        saveFile('tasks.txt', files[t - 1])
                        print("Task removed successfully!")
                        printTasks(files[t - 1])
                elif t == 2:
                    printTasks(files[t - 1])
                    while True:
                        try:
                            n = int(input("Enter the number of the task to remove: "))
                            break
                        except ValueError:
                            print("ERROR: Invalid number")
                    if n < 1 or n > len(files[t - 1]):
                        print("Invalid task number")
                    else:
                        del files[t - 1][n - 1]
                        saveFile('tasks_completed.txt', files[t - 1])
                        print("Task removed successfully!")
                        printTasks(files[t - 1])
        elif m == 4: 
            printTasks(tasks)
            while True:
                try:
                    n = int(input("Enter the number of the task to be marked as completed: "))
                    break
                except ValueError:
                    print("ERROR: Invalid number")
            if n < 1 or n > len(tasks):
                print("Invalid task number")
            else:
                compl.append(tasks[n - 1])
                del tasks[n - 1]
                saveFile('tasks_completed.txt', compl)
                saveFile('tasks.txt', tasks)
                print("Task marked successfully!")
                printTasks(tasks)
        elif m == 5:
            print("Goodbye")
            break
        else:
            print("Try again")

menu()