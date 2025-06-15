for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    q=[]
    ans=[]
    for i in range(len(arr)):
        while q and arr[q[-1]]<arr[i]:
            q.pop()
        q.append(i)
        if i-q[0]>=k:
            q.pop(0)
        if i>=k-1:
            ans.append(arr[q[0]])
    print(ans)
