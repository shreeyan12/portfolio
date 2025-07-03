# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"✅ '{task}' added to your to-do list.")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("📭 Your to-do list is empty.")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter the number of the task to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"❌ '{removed}' removed from your list.")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Main menu loop
while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("👋 Goodbye! Happy productivity!")
        break
    else:
        print("❗ Invalid choice. Please enter 1, 2, 3, or 4.")
