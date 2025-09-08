#1,2,3,3,4,4,5,5
n=int(input())
arr=[int(x) for x in input().split()]
dp=[[-1 for i in range(n)] for j in range(n)]
path=[[-1 for i in range(n)] for j in range(n)]


def fun(index, left_index):

    if index == n - 1:
        return max(arr[index], arr[left_index])
    if index == n:
        return arr[left_index]
    if dp[index][left_index]!=-1:
        return dp[index][left_index]

    # Calculate all options
    options = [
        fun(index + 2, index + 1) + max(arr[index], arr[left_index]),  # option 0
        fun(index + 2, left_index) + max(arr[index], arr[index + 1]),  # option 1
        fun(index + 2, index) + max(arr[left_index], arr[index + 1])  # option 2
    ]

    # Find best option and store both value and path
    best_idx = options.index(min(options))
    # print(index,left_index,best_idx,options[best_idx])
    dp[index][left_index] = options[best_idx]
    path[index][left_index] = best_idx

    return dp[index][left_index]


def helper(index, prev_index):
    if index == n - 1:
        print(index+1, prev_index+1)  # Convert to 1-based
        return
    if index == n:
        print(prev_index+1)  # Convert to 1-based
        return

    option = path[index][prev_index]

    if option == 0:  # Take prev_index and index
        print(prev_index+1, index+1)  # Convert to 1-based
        if index + 1 < n:
            helper(index + 2, index + 1)
        else:
            print(index + 2) if index + 1 < n else None  # Convert to 1-based
    elif option == 1:  # Take index and index+1
        print(index+1, index + 2)  # Convert to 1-based
        helper(index + 2, prev_index)
    elif option == 2:  # Take prev_index and index+1
        print(prev_index+1, index + 2)  # Convert to 1-based
        helper(index + 2, index)


# Call it without passing option parameter
print(fun(1, 0))
# print(fun(3,2))
helper(1, 0)
