import os
import time
import threading

# menu of todo items
def todo_menu():
    print("Welcome to the Todo Application Menu ::")
    print("1. Add Todo Item")
    print("2. View Todo Items")
    print("3. Update Todo Item")
    print("4. Remove Todo Item")
    print("5. Exit")

def load_todos():
    try:
        with open('todos.txt', 'r') as file:
           return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_todo(todo_list):
    with open('todos.txt', 'w') as file:
        for item in todo_list:
            file.write(f"{item}\n")

# Function to add a todo item
def main():
    def watch_todos_file(callback, interval=1):
        last_mtime = None
        while True:
            try:
                mtime = os.path.getmtime('todos.txt')
                if last_mtime is None:
                    last_mtime = mtime
                elif mtime != last_mtime:
                    last_mtime = mtime
                    callback()
            except FileNotFoundError:
                pass
            time.sleep(interval)

    def refresh_task_list():
        nonlocal task_list
        task_list = load_todos()

    watcher_thread = threading.Thread(target=watch_todos_file, args=(refresh_task_list,), daemon=True)
    watcher_thread.start()
    
    task_list = load_todos()  # load todos from file
    while True:
        todo_menu()  # display the todo menu
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            todo_item = input("Enter a new task to save: ")
            task_list.append(todo_item)
            save_todo(task_list)
            print(f"Todo item '{todo_item}' added successfully.")

        elif choice == '2':
            if not task_list:
                print("No todo items found.")
                continue
            print("Todo Items:")
            for i, item in enumerate(task_list, start=1):
                print(f"{i}. {item}")

        elif choice == '3':
            if not task_list:
                print("No todo items to update.")
                continue
            print("Todo Items:")
            for i, item in enumerate(task_list, start=1):
                print(f"{i}. {item}")
            index = int(input("Enter the number of the item to update: ")) - 1
            if 0 <= index < len(task_list):
                new_item = input("Enter the updated task: ")
                task_list[index] = new_item
                save_todo(task_list)
                print(f"Todo item updated to '{new_item}'.")
            else:
                print("Invalid item number.")

        elif choice == '4':
            if not task_list:
                print("No todo items to remove.")
                continue
            print("Todo Items:")
            for i, item in enumerate(task_list, start=1):
                print(f"{i}. {item}")
            index = int(input("Enter the number of the item to remove: "))
            removed_item = task_list.pop(index-1)
            save_todo(task_list)
            print(f"Todo item '{removed_item}' removed successfully.")

        elif choice == '5':
            print("Exiting the Todo Application. Goodbye!")
            break

        else:
            print("Invalid item number.")

# to run the todo application
if __name__ == "__main__":
    main()