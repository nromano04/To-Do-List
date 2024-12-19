#To-do List Application
#Author: Nick Romano

def add_task(task_list):
    task_name = input("Enter the task: ")
    task_list.append({"task": task_name, "completed": False})
    print("Task added!")


def view_tasks(task_list):
    if not task_list:
        print("No tasks to display!")
    else:
        for num, task in enumerate(task_list):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{num + 1}. {task['task']} - {status}")


def mark_task_completed(task_list):
    view_tasks(task_list)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(task_list):
        task_list[task_number]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number!")


def delete_task(task_list):
    view_tasks(task_list)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(task_list):
        del task_list[task_number]
        print("Task deleted!")
    else:
        print("Invalid task number!")


def save_tasks(task_list):
    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(f"{task['task']}|{task['completed']}\n")


def load_tasks():
    task_list = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_name, completed = line.strip().split("|")
                task_list.append({"task": task_name, "completed": completed == "True"})
    except FileNotFoundError:
        print("No previous tasks found.")
    return task_list


def main():
    task_list = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            mark_task_completed(task_list)
        elif choice == '4':
            delete_task(task_list)
        elif choice == '5':
            save_tasks(task_list)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
