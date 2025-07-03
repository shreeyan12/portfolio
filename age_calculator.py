age = input("Enter your birth year: ")
age = 2025 - int(age)

age_m = age * 12
age_d = age * 365
age_s = age_d*24*60*60

print(f"You are {age} years old.")
print(f"You are {age_m} months old")
print(f"You are {age_d} days old")
print(f"You are {age_s} seconds old")



