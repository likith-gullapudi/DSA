# Function to find the total time required by Kotivalo and Justiina to read all the books
def solve(arr):
    # Sort the books in increasing order of their reading times
    arr.sort()

    # Store the largest reading time
    largest = arr[-1]

    # Store the sum of remaining times
    sumOfSmaller = sum(arr[:-1])

    # If largest <= sumOfSmaller, then none of them will have to wait
    # and answer will be the sum of reading times of all the books
    if largest <= sumOfSmaller:
        return sumOfSmaller + largest
    # Otherwise, one of them has to wait and the answer will be 2 * largest reading time
    return 2 * largest

# Driver code
n=int(input())
arr = [int(x) for x in input().split()]
print(solve(arr))