# Store student data as a list of tuples
students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    student = (name, age, marks)
    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("❌ No students found.\n")
        return
    print("\n📋 All Student Records:")
    for s in students:
        print(f"Name: {s[0]}, Age: {s[1]}, Marks: {s[2]}")
    print()

def search_student():
    search_name = input("Enter name to search: ")
    found = False
    for s in students:
        if s[0].lower() == search_name.lower():
            print(f"🎯 Found: Name: {s[0]}, Age: {s[1]}, Marks: {s[2]}")
            found = True
            break
    if not found:
        print("❌ Student not found.\n")

def main():
    while True:
        print("🎓 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Try again.\n")

# Run the main menu
main()
