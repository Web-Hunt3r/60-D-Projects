import sys
import time
print("     --------Welcome to T0-D0 Lista--------")
print("         | Your Tasks. Your Terminal |        ")

time.sleep(1.5)
task_list = []

print(" 0. View TaskList \n 1. Add a task to tasklist " \
"\n 2. Remove a Task \n 3. Mark task as completed \n " \
"4. Mark task as pending\n 5. Exit\n\n")
while True:
    choice = input("Your Choice = ") 
    
    if choice=="0":
        print("\n--- Your Task List ---")
        if not task_list:
            print("No tasks yet!")
        else:
            for index, task in enumerate(task_list):
                status = "✓" if task["done"] else "✗"
                print(f"{index + 1}. [{status}] {task['title']}")
                print(f"    ↪ {task['text']}")

    elif choice=="1":
        task_title= input("Enter task title: ")
        task_text = input("Enter  task description: ")
        task_list.append({"title": task_title, "text": task_text, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if not task_list:
            print("Lazy bastard, write something firstt!")
        else:
            for index, task in enumerate(task_list):
                print(f"{index + 1}. {task['title']}")
            remove_index = int(input("Enter task id to remove: ")) - 1
            if 0 <= remove_index < len(task_list):
                removed = task_list.pop(remove_index)
                print(f"Removed task: {removed['title']} \n")
            else:
                print("Invalid input, dummy!\n")

    elif choice == "3":
        if not task_list:
            print("No tasks to mark as completed!\n")
        else:
            for index, task in enumerate(task_list):
                print(f"{index + 1}. {task['title']} - {'Done' if task['done'] else 'Pending'}")
            mark_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= mark_index < len(task_list):
                task_list[mark_index]["done"] = True
                print(f"Woah...Task completed: {task_list[mark_index]['title']}\n")
            else:
                print("Jesuss...watch your keyboard, you dummy!\n")
    
    elif choice == "4":
        if not task_list:
            print("No tasks to mark as pending!\n")
        else:
            for index, task in enumerate(task_list):
                print(f"{index + 1}. {task['title']} - {'Done' if task['done'] else 'Pending'}")
            mark_index = int(input("Enter the task number to mark as pending: ")) - 1
            if 0 <= mark_index < len(task_list):
                task_list[mark_index]["done"] = False
                print(f"Marked as pending: {task_list[mark_index]['title']}\n")
            else:
                print("Invalid task number!\n")


    elif choice== "5":
        sys.exit(0)


