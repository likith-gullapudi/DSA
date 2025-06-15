n=int(input())
arr=[int(x) for x in input().split()]
st=[]
ans=[]
for i in range(len(arr)):
    while st and arr[st[-1]]>=arr[i]:
        st.pop()
    ans.append(st[-1]+1 if st else 0)
    st.append(i)
for i in ans:
    print(i,end=" ")
