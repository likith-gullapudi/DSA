
def nex(arr):
    stack=[]
    ans=[]
    for i in range(len(arr)-1,-1,-1):
        while stack!=[] and stack[-1][0]>=arr[i]:
            stack.pop()
        if stack==[]:
            ans.append(len(arr))
        else:
            ans.append(stack[-1][1])
        stack.append([arr[i],i])
    return list(reversed(ans))
def prev(arr):

    stack = []
    ans = []
    for i in range(len(arr)):
        while stack != [] and stack[-1][0] >= arr[i]:
            stack.pop()
        if stack == []:
            ans.append(-1)
        else:
            ans.append(stack[-1][1])
        stack.append([arr[i], i])
    return ans
for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    matrix=[]
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    ans=0
    print(matrix)
    for arr in matrix:
        prev_small=prev(arr)
        next_small=nex(arr)
        #print(prev_small,next_small,arr)
        for i in range(len(arr)):
            ans=max(ans,(next_small[i]-prev_small[i]-1)*int(arr[i]))
    print(ans)