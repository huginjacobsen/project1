print ("Hugin2ádev")

def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operation = input ("What would you like to do?")
n1 = int(input("Choose a number:"))
n2 = int(input("Choose a second number:"))

if operation == "+":
     result = add(n1, n2)
elif operation == "-":
    result = minus(n1, n2)

print(result)
print("Done")

