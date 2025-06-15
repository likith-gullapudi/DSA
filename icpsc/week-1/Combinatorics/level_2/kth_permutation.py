import itertools

s="aabb"
temp=set(itertools.permutations(s))
temp=sorted(temp)
for i in temp:
    print(i)