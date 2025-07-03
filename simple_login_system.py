print("SignUp")

signup_user = input("Enter your username: ")
signup_password = input("Enter your password: ")

print("\nLogIn")
login_user = input("Enter your username: ")

if login_user == signup_user:
    a = 3
    while a>0:
        login_password = input("Enter your password: ")
        if login_password == signup_password:
            print("✅ Login successful!")
            break
        else:
            a -= 1
            if a>0:
                print(f"Wrong password {a} attempts left")
            else:
                print("⛔ Access denied.")
else:
    print("username not found!")
