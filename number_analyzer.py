numbers = [4, 7, 2, 9, 4, 1, 6, 3]
largest = numbers[0]
smallest = numbers[0]
even_sum = 0
odd_count = 0
seen = []
has_duplicate = False
reversed_list = []

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    if num % 2 == 0:
        even_sum = even_sum + num
    else:
        odd_count = odd_count + 1
    if num in seen:
        has_duplicate = True
    seen.append(num)

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
print(f"Even sum: {even_sum}")
print(f"Odd count: {odd_count}")
print(f"Duplicates: {has_duplicate}")
print(f"Reversed: {reversed_list}")
