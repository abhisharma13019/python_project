def task():
    tasks = []
    print("*********Welcome To The Task Management App**********")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are:\n{tasks}")

    while True:
        operation = int(input("Enter\n 1-ADD\n 2-Update\n 3-Delete\n 4-View\n 5-Exit\n"))

        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")
        
        elif operation == 2:
            update = input("Enter the task name you want to update = ")
            if update in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f"Updated task to: {up}")
            else:
                print("Task not found!")
        
        elif operation == 3:
            delete_val = input("Which task you want to delete = ")
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f"Task '{delete_val}' has been deleted.")
            else:
                print("Task not found!")
        
        elif operation == 4:
            print(f"Current tasks: {tasks}")
        
        elif operation == 5:
            print("Closing the program...")
            break
        
        else:
            print("Invalid input!")

# Function call
task()
