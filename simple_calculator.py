a = float(input('Enter first number '))
op = input('Enter the operator + - * / ')
b = float(input('Enter the second number '))

if op =='+':
    print(a+b)
elif op =='-':
    print(a-b) 
elif op =='*':
    print(a*b)
elif op =='/':
    if b != 0:
        print(a/b)
    else:
        print('Number not divisible by zero')
else:
    print('Invalid Operator!')