import sys
ans=[]
def rec(left,right):
    #base case
    if right==0:
        print("".join(ans))
        return
    #choices
    if left>0:
        #set
        ans.append("(")
        rec(left-1,right)
        ans.pop()
    if right>left:
        ans.append(")")
        rec(left,right-1)
        ans.pop()
n=int(sys.stdin.readline().strip())
rec(n//2,n//2)
