word = input("Enter a word to count => ").strip().replace(" ","")
word_count = 0

for letters in word:
    word_count += 1 

print(word_count)
