rows = 5
i = 1
while i <= rows:
    spaces = rows-i
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    stars = 1
    while stars <= i:
        print("*", end="")
        stars += 1
    print()
    i += 1        