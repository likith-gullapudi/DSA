import sys

# Read integers n and k from a single line separated by space
n, k = map(int, sys.stdin.readline().split())
ans=[]
def rec(left,right,ma):
    #base
    if right==n//2:
        if ma==k:
            print("".join(ans))
        return
    if left<n//2 and left-right<k:
        ans.append("(")
        rec(left+1,right,max(ma,left-right))
        ans.pop()
    if right<left:
        ans.append(")")
        rec(left,right+1,max(ma,left-right))
        ans.pop()
    return
rec(0,0,0)
