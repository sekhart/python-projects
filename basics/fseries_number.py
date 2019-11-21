numbers = [0, 1]

for i in range(2, 10):
    numbers.append(numbers[i - 1] + numbers[i - 2])
for number in numbers:
    print(number)
