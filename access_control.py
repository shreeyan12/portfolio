a = input("Are you over 18? (Yes/No): ").strip().lower() == "yes"
b = input("Do you have an ID card? (Yes/No): ").strip().lower() == "yes"

if a and b:
    print("Entry allowed.")
else:
    print("Entry denied.")

