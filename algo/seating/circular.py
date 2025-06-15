import itertools


# Helper functions
def left(a, b, dist, arrangement):
    n = len(arrangement)
    idx_a = arrangement.index(a)
    idx_b = arrangement.index(b)
    return (idx_b - idx_a) % n == dist


def right(a, b, dist, arrangement):
    n = len(arrangement)
    idx_a = arrangement.index(a)
    idx_b = arrangement.index(b)
    return (idx_a - idx_b) % n == dist


def between(a, b, c, arrangement):
    n = len(arrangement)
    idx_a = arrangement.index(a)
    idx_b = arrangement.index(b)
    idx_c = arrangement.index(c)

    #print((arrangement[(idx_c-1)%n]==a and arrangement[(idx_c+1)%n]==b) or (arrangement[(idx_c+1)%n]==a and arrangement[(idx_c-1)%n]==b))
    return (arrangement[(idx_c-1)%n]==a and arrangement[(idx_c+1)%n]==b) or (arrangement[(idx_c+1)%n]==a and arrangement[(idx_c-1)%n]==b)



# Variables
people = [i for i in 'KLMNOPQ']
permutations = list(itertools.permutations(people))

# # Check each permutation
for arrangement in permutations:
    if (left('L', 'Q', 2, arrangement) and
            right('P', 'K', 1, arrangement) and
            between('K', 'N', 'O', arrangement) and
            not between('P','M','Q',arrangement) ):
        print("Valid arrangement found:", arrangement)
        break
else:
    print("No valid arrangement found")
arrangement=[i for i in 'NOKPLMQ']
print( (left('L', 'Q', 2, arrangement) ,
            right('P', 'K', 1, arrangement) ,
            between('K', 'N', 'O', arrangement) ,
            not between('P','M','Q',arrangement) ))
