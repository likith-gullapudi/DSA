for _ in range(int(input())):
    n=int(input())
    ans=0
    arr=[int(x) for x in input().split()]
    #for every element find next and prev smaller
    def prev_lesser(arr,n):
        st = []
        ans = [-1 for i in range(n)]
        fans=[n for i in range(n)]
        i = 0
        while i < n:
            while st and arr[st[-1]] >= arr[i]:
                temp=st.pop()
                fans[temp]=i
            if st:
                ans[i]=st[-1]

            st.append(i)
            i += 1
        return [ans,fans]
    x,y=prev_lesser(arr,n)


    for i in range(n):
        ans += arr[i] * (i - x[i]) * (y[i] - i);

    print(ans)



