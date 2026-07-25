def find_max(numbers):
    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest

result = find_max([3, 7, 2, 9, 4])
print(result)
