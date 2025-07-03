def calculator():
    a = float(input("Enter first number: "))
    op = input("Enter the operator (+, -, *, /, //, %, **): ")
    b = float(input("Enter second number: "))

    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b if b != 0 else "Cannot divide by zero!")
    elif op == '//':
        print(a // b if b != 0 else "Cannot divide by zero!")
    elif op == '%':
        print(a % b)
    elif op == '**':
        print(a ** b)
    else:
        print("Invalid Operator!")

calculator()
