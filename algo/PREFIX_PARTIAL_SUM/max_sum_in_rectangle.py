n,m,q=[int(x) for x in input().split()]
arr=[[0 for i in range(m+2)] for j in range(n+2)]
for _ in range(q):
    x1,y1,x2,y2,c=[int(x) for x in input().split()]
    arr[x1][y1]+=c
    arr[x2+1][y1]-=c
    arr[x1][y2+1]-=c
    arr[x2+1][y2+1]+=c
for i in range(1,n+1):
    for j in range(1,m+1):
        arr[i][j]+=arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]
max_value = float('-inf')

# Iterate over each row in the 2D array
for row in arr:
    # Iterate over each element in the row
    for num in row:
        # Update max_value if the current element is greater
        if num > max_value:
            max_value = num
count=0
for row in arr:
    # Iterate over each element in the row
    for num in row:
        # Update max_value if the current element is greater
        if num == max_value:
            count+=1
print(max_value,count)
