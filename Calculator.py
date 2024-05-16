def add(x, y): 
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("Select the operation:")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter your option (1/2/3/4): ")

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid operation")
