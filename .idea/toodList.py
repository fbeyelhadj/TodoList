

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            completed_task = self.tasks.pop(index)
            print(f"Task marked as completed: {completed_task}")
        else:
            print("Invalid task index")

    def display_todo_list(self):
        if not self.tasks:
            print("Todo list is empty")
        else:
            print("Todo List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Program")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display Todo List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_task = input("Enter task to add: ")
            todo_list.add_task(new_task)
        elif choice == '2':
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(task_index)
        elif choice == '3':
            todo_list.display_todo_list()
        elif choice == '4':
            print("Exiting Todo List Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
