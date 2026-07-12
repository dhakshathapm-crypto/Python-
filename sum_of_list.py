def sum_list(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

numbers = [4, 7, 10, 3, 8]
print(sum_list(numbers))
