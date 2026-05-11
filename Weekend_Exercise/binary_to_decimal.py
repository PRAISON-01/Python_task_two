binary = int(input('Enter a binary number => '))
x = binary

decimal_value = 0
power = 0
calculate = 0
while binary > 0:
    digit = binary % 10
    calculate  = digit * pow(2, power)
    decimal_value += calculate
    binary //= 10
    power += 1

print("Binary -----> Decimal")
print(f"{x}   -----> {decimal_value}")


