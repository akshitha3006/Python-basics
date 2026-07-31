valid = False
try:
    n=int(input("Enter a number:"))
    while n%2==0:
        print("Bye Bye")
    valid = True
except ValueError:
    print("Invalid input. Please enter a valid integer.")