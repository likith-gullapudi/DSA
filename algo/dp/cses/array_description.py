# n,m=[int(x) for x in input().split()]
# arr=[int(x) for x in input().split()]
# dp=[[0 for i in range(m+1)] for j in range(n+1)]
# next=[0 for i in range(m+1)]
#
# for index in range(n,0,-1):
#     present=[0 for i in range(m+1)]
#     for prev in range(1,m+1):
#         if index==n:
#             present[prev]=1
#         else:
#             if arr[index]==0:
#                 for diff in range(-1,2):
#                     curr=prev+diff
#                     if 1<=curr<=m:present[prev]+=next[curr]%(10**9+7)
#             else:
#                 curr=arr[index]
#                 if abs(curr-prev)<=1:
#                     present[prev]=next[curr]%(10**9+7)
#     next=present[:]
#
# ans=0
# if arr[0]==0:
#     for curr in range(1,m+1):
#         ans+=next[curr]%(10**9+7)
# else:
#     curr=arr[0]
#     ans+=next[curr]%(10**9+7)
# print(ans%(10**9+7))



