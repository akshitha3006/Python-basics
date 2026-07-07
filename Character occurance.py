string=input("Enter your word:")
char=input("Enter the letter:")
i = 0
count = 0
while i < len(string):
    if (string[i]== char):
        count = count+1
    i = i+1
print("The letter",char,"has occured",count,"times")        
