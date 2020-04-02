#Take user input and pass to function.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

def add(num1, num2):
    solution = num1 + num2
    return f"{num1} + {num2} = {solution}"


print(add(num1, num2 ))
