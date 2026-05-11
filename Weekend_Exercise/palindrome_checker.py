number = int(input("Enter a number => "))
x = number

reverse = 0
while number > 0:
    digits = number % 10
    reverse = (reverse * 10) + digits
    number = number // 10


if x == reverse:
    print(f"{reverse} is a palindrome")
else:
    print(f"{reverse} is 'NOT' a palindrome")

