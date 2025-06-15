def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Usage
counter = count_up_to(5)
print(counter)
print(next(counter))
print(next(counter))
