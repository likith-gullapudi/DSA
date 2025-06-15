for i in range(int(input())):
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    d={}
    for i in arr:
        d[i]+=1
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    
