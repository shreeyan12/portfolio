contacts = {}
def add_contacts():
    name = input("Enter your contact name: ")
    number = input("Enter you phone number: ")
    contacts[name] = number
    print(f"✅ Contact '{name}' added.")

def view_contacts():
    if not contacts:
        print("📭 No contacts found")
    else:
        print("\n📒 Contact Lists: ")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def search_contacts():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"🔍{name}'s number is {contacts[name]}")
    else:
        print("❌no contacts found")

def delete_contacts():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️contact '{name}' deleted.")
    else:
        print("❌no contacts found")

while True:
    print("\n=========Contact Book Menu==========")
    print("1. Add Contacts")
    print("2. View all Contacts")
    print("3. Search Contacts")
    print("4. Delete Contacts")
    print("5. Exit")

    choice = input("choose an option (1-5)")

    if choice == '1':
        add_contacts()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contacts()
    elif choice == '4':
        delete_contacts()
    elif choice == '5':
        print("Exiting contact book. Bye!")
        break
    else:
        print("Invalid choice. Please try again")

    