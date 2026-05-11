number = int(input("Enter a number => "))
x = number

binary_total =""

while number >= 1:
    reduction = number % 2
    binary_total = str(reduction) + binary_total
    number //= 2

print("Decimal -----> Binary(baseTwo)")
print(f" {x} ----->  {binary_total} ")
