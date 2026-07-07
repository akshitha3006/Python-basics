lower=int(input("Enter the starting number:"))
upper=int(input("Enter the ending number:"))
print("The prime numbers between",lower,"and",upper,"is:")
for num in range(lower,upper+1):
    if num >1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
                print(num)
