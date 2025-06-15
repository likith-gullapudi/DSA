for _ in range(int(input())):
    n,m=[int(x) for x in input().split()]
    arr=[[] for i in range(n)]
    for _ in range(m):
        x,y=[int(x)-1 for x in input().split()]
        arr[x].append(y)
    print(arr)
    visited=[1 for i in range(n)]
    '''
    1 means not visited
    2 means in path now
    3 means already completed
    '''
    cycle=False
    def dfs(i,par):
        global cycle
        visited[i]=2
        for nei in arr[i]:
            if nei==par:
                continue

            if visited[nei]==1:
                dfs(nei,i)
            elif visited[nei]==2:
                cycle=True
            elif visited[nei]==3:
                a=1 #do nothing
        visited[i]=3


    for i in range(n):
        if visited[i]==1:
            dfs(i,-1)
    if cycle:
        print("YES")
    else:
        print('NO')
