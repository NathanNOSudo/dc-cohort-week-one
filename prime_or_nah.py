a = input('inter a number: ')
s = 0
if a == 1:  
    print(a, 'is a prime')

else : 

    for i in range (2, a ):

        if a%i == 0:
            print(a,' is not a prime number')
            s = 'true'
            break

    if s == 0 : print(a,' is a prime number')
