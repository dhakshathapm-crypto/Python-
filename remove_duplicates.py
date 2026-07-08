numbers = [1, 2, 3, 2, 4, 1, 5]
seen = []
result = []

for num in numbers:
    if num not in seen:
        result.append(num)
        seen.append(num)

print(result)
