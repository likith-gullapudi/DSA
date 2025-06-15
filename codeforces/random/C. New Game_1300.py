


for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    d={}
    for val in arr:
        d[val]=d.get(val,0)+1

    sorted_keys=sorted(d.keys())
    i,j=0,0

    least=sorted_keys[0]
    ans=fans=d[least]

    for i in range(1,len(sorted_keys)):
        key=sorted_keys[i]
        prev_key=sorted_keys[i-1]
        if key-prev_key!=1:
            ans=d[key]
            least=key
        else:
            if key-least+1>k:
                ans-=d[least]
                least+=1
            ans+=d[key]
        fans=max(ans,fans)
    print(fans)
