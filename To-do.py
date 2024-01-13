class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[len(self.tasks) + 1] = {"task": task, "status": "Not Done"}

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for task_id, task_info in self.tasks.items():
                print(
                    f"{task_id}. {task_info['task']} - Status: {task_info['status']}")

    def update_status(self, task_id, new_status):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = new_status
            print(f"Status of Task {task_id} updated to: {new_status}")
        else:
            print("Invalid task ID.")


todo_list = TodoList()

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Status")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
    elif choice == "2":
        todo_list.view_tasks()
    elif choice == "3":
        todo_list.view_tasks()
        task_id = int(input("Enter the task ID to update status: "))
        new_status = input(
            "Enter the new status (e.g., 'Done' or 'Not Done'): ")
        todo_list.update_status(task_id, new_status)
    elif choice == "4":
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
