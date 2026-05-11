word = input("Enter  a word => ")

count = 0
for letter in word:
    if letter == letter.upper():
        count += 1

print(f"Uppercase count => {count}")
