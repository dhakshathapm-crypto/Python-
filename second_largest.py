numbers = [10, 5, 20, 8, 20, 3]
biggest = numbers[0]
second_biggest = 0

for num in numbers:
    if num > biggest:
        second_biggest = biggest
        biggest = num

print(biggest)
print(second_biggest)
