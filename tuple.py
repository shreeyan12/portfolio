student_names = ("Ram", "Hari", "Krishna", "Shubham", "Gopal")

hobbies = set()
print("Enter at least 5 hobbies, one by one. Type 'done' when finished.")
while len(hobbies) < 5:
    hobby = input("Enter a hobby: ")
    if hobby.lower() == 'done':
        break
    hobbies.add(hobby)

print("\nStudent Names:")
for name in student_names:
    print(name)

print(f"\nTotal number of unique hobbies: {len(hobbies)}")

if len(hobbies) >= 5:
    print("This class has very diverse interests!")
