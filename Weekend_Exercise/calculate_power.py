number = int(input("Enter a number => "))

power_size = int(input("Enter power of number => "))

index = 1
while index < power_size + 1:
    result = number ** index
    index += 1

print(result)
