def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count

numbers = [4, 7, 10, 3, 8]
print(count_even(numbers))
