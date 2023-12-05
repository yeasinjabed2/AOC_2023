inputs = open('day-01/1-input.txt', 'r').read().split('\n')

total_sum = 0

for input in inputs:
    digits = []
    for char in input:
        if char.isdigit():
            digits.append(char)

    total_sum += int(digits[0] + digits[-1])

print(total_sum)  # 53386
