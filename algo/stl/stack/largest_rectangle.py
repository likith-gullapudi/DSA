for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    #find next lesser and next greater for every element
    #finding prev lesser
    def prev_lesser(arr,n):
        st = []
        ans = []
        fans=[n for i in range(n)]
        i = 0
        while i < n:
            while st and arr[st[-1]] >= arr[i]:
                temp=st.pop()
                fans[temp]=i
            ans.append(-1 if st == [] else st[-1])
            st.append(i)
            i += 1
        return [ans,fans]
    # def next_lesser(arr,n):
    #     st=[]
    #     ans=[n for i in range(n)]
    #     i=n-1
    #     while i>=0:
    #         while st and arr[st[-1]] >= arr[i]:
    #             st.pop()
    #         if st:
    #             ans[i]=st[-1]
    #         st.append(i)
    #         i -= 1
    #     return ans
    #x,y=next_lesser(arr,n)
    x,y=prev_lesser(arr,n)
    #print(x,y)
    ans=-float('inf')
    for i in range(len(arr)):
        ans=max(ans,(arr[i]*(y[i]-x[i]-1)))
    print(ans)

