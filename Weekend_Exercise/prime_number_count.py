prime_count = 0
for number in range(2, 101):
    for num in range(2, number):
        if number % num  == 0:
            break
    else:
        prime_count += 1
        print(number)
print(f"There are {prime_count} prime numbers  from 1 to 100")
