import itertools


# Helper functions for non-circular arrangement
def left(a, b, dist, arrangement):
    idx_a = arrangement.index(a)
    idx_b = arrangement.index(b)
    return idx_b - idx_a == dist


def right(a, b, dist, arrangement):
    idx_a = arrangement.index(a)
    idx_b = arrangement.index(b)
    return idx_a - idx_b == dist


def between(a, b, c, arrangement):
    idx_a = arrangement.index(a)
    idx_b = arrangement.index(b)
    idx_c = arrangement.index(c)

    # Check if b is between a and c
    return (idx_a+2 == idx_b+1 == idx_c) or (idx_c+2 == idx_b+1 == idx_a)


# Variables
people = [i for i in 'ABCDEFG']
permutations = list(itertools.permutations(people))

# Check each permutation
for arrangement in permutations:
    if (left('B', 'C', 1, arrangement) and
       right('D', 'C', 1, arrangement) and
       between('E', 'F', 'A', arrangement) and arrangement.index('B')==1 and arrangement.index('A')==7-1) :
        print("Valid arrangement found:", arrangement)
        break
else:
    print("No valid arrangement found")

# Example arrangement to check
arrangement = [i for i in 'ABCDEF']
print((left('B', 'C', 1, arrangement) ,
       right('A', 'B', 1, arrangement) ,
       between('E', 'F', 'A', arrangement) , arrangement.index('B')==1 and arrangement.index('A')==7-1))

