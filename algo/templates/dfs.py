'''function dfs(node, state):
    if node is null:
        ...
        return

    left = dfs(node.left, state)
    right = dfs(node.right, state)

        ...

    return ...
'''
def dfs(x,y):
    visited[x][y]=True
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        xx,yy=dx+x,dy+y
        if is_valid(xx,yy) and  arr[xx][yy]=="." and not visited[xx][yy]:
            dfs(xx,yy)


