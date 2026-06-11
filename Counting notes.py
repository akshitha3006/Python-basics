amount= int(input("Enter the amount: "))
notes_100 = amount//100
notes_50 = (amount%100)//50
notes_10 = ((amount%100)%50)//10
print("The total number of 100 notes is", notes_100)
print("The total number of 50 notes is", notes_50)
print("The total number of 10 notes is", notes_10)
