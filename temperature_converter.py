print("Temperature Converter")
print("Type 1 to convert Celsius to Fahrenheit")
print("Type 2 to convert Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    t_c = float(input("Enter temperature in Celsius: "))
    t_f = (t_c * 9/5) + 32
    print(t_c, "degrees Celsius is", t_f, "degrees Fahrenheit.")
elif choice == "2":
    t_f = float(input("Enter temperature in Fahrenheit: "))
    t_c = (t_f - 32) * 5/9
    print(t_f, "degrees Fahrenheit is", t_c, "degrees Celsius.")
else:
    print("Invalid choice. Please enter 1 or 2.")
