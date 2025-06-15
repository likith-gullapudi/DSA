for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    st=[]
    ans=[]
    i=0
    while i<n:
        while st and arr[st[-1]]>=arr[i]:
            st.pop()
        ans.append('0' if st==[] else str(st[-1]+1))
        st.append(i)
        i+=1
    print(" ".join(ans))