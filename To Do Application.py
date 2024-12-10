# #create a to do list
# task_menu = ["Add tasks", "View tasks", "Delete tasks", "Quit the application"]

tasks = [] 

# To-Do List Application
#create a list menu as a function
# Function to display the menu
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Quit")

# Function to add a task
def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty.")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks to show. Your to-do list is empty.")

# Function to delete a task
def delete_task():
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted!")
            else:
                print("Task number out of range.")
        except ValueError:
            print("Invalid input! Please enter a valid task number.")
    else:
        print("No tasks to delete. Your to-do list is empty.")

# Main function to run the application
def run_todolist_app():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-4).")

# Run the application
run_todolist_app()
