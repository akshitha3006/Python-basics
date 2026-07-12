print("Lets play a number guessing game:")
print("You have 5 lives to guess the correct number")
print("Your hints are:\n1. Cold if your number is  greater than the secret number\n  2. Warm if you number is lower than the secret number")
i = 5
while i>0:
num =int(input("Enter a number between 1 and 50:"))

secret =36

if num >1 and num<50:
        if num==secret:
            print("You guessed the correct number")
            break

elif num>secret:
            print("Cold,try again")
            print("you have ",i-1,"lives left")
            
else:
            print("Warm,try again")
            print("you have ",i-1,"lives left")
            

    
