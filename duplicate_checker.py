numbers = [1, 2, 3, 2, 5]
seen = []
has_duplicate = False   # starts assuming no duplicates

for num in numbers:
    if num in seen:
        has_duplicate = True   # flip it if we find one
    seen.append(num)

print(has_duplicate)
