a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
d=[int(x) for x in input().split()]
print(len(a),len(c))
for index,(i,j) in  enumerate(zip(a,c)):
    if i!=j:
        print(index)