contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("✅ Contact saved.\n")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        print("❌ Contact not found.\n")

def main():
    while True:
        print("📱 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice!\n")

main()
