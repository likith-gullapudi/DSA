'''
Time limit: 1.00 s
Memory limit: 512 MB



Find the middle element when the numbers in an n \times n multiplication table are sorted in increasing order. It is assumed that n is odd.
For example, the 3 \times 3 multiplication table is as follows:
$$
\begin{matrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
3 & 6 & 9 \\
\end{matrix}
$$
The numbers in increasing order are [1,2,2,3,3,4,6,6,9], so the answer is 3.
Input
The only input line has an integer n.
Output
Print one integer: the answer to the task.
Constraints

1 \le n < 10^6

Example
Input:
3

Output:
3
'''
def check(val):
    ans=0
    for i in range(1,n+1):
        ans+=min(n,val//i)


    return ans>=((n*n)//2)+1

n=int(input())
lo,hi=1,n*n
ans=-1
while lo<=hi:
    mid=(lo+hi)//2
    temp=check(mid)

    if temp:
        ans=mid
        hi=mid-1
    else:
        lo=mid+1
print(ans)