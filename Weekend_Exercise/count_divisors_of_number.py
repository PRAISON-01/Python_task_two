number = int(input("Enter a number => "))

count = 0
for divisor in range(1, number + 1):
    if number % divisor == 0:
        count += 1

print(f"{count} numbers can divide {number}  without a remainder")
