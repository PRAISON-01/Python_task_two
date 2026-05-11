word = input('Enter a number word => ')
s = word
reverse =""
for letter in word:

    reverse = letter + reverse

if s == reverse:
    print(f"{reverse} is palindrome string")
else:
    print(f"{reverse} is not a palindrome string")
