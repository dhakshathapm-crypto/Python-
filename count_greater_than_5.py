def count_greater_than(numbers, limit):
    count = 0
    for number in numbers:
        if number > limit:
            count += 1
    return count

print(count_greater_than([8, 15, 2, 9], 5))
