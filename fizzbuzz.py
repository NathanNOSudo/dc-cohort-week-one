number = int(input("Enter a number: "))


def fizzbuzz(number):
    n = 1
    while n <= number:
        if n % 3 != 0 and n % 5 != 0:
            print(n)
        elif n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 3 == 0:
            print("fizz")
        elif n % 5 == 0:
            print("buzz")
        n = n + 1
    return number

fizzbuzz(number)
