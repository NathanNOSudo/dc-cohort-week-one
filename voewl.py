#Codewars print number of vowels in a string 
#changed to accept a user input

string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=="Y"):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
