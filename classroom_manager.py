classroom = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    classroom[roll] = {"name": name, "age": age, "marks": marks}
    print("✅ Student added.\n")

def view_classroom():
    if not classroom:
        print("❌ No students added yet.\n")
    else:
        for roll, info in classroom.items():
            print(f"Roll: {roll}")
            for key, val in info.items():
                print(f"  {key}: {val}")
        print()

def search_student():
    roll = input("Enter roll number to search: ")
    if roll in classroom:
        print("🎯 Student found:")
        for key, value in classroom[roll].items():
            print(f"{key}: {value}")
    else:
        print("❌ Student not found.\n")

def main():
    while True:
        print("🎓 Classroom Manager")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search by Roll")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_classroom()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice.\n")

main()
