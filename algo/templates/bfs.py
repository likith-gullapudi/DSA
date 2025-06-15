def bfs(node):
    visited[node]=True
    q=deque([node])
    while q:
        temp=q.popleft()
        #print(q, visited, temp)

        for nei in arr[temp]:
            if not visited[nei]:
                visited[nei]=True
                q.append(nei)

#if tree connectinos will be just left and right