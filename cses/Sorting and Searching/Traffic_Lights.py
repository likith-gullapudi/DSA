from sortedcontainers import SortedList

# def just_smaller(points,val):
#     #print(val)
#     lo,hi=0,len(points)-1
#     ans=-1
#     while lo<=hi:
#         mid=(lo+hi)//2
#         if points[mid]<=val:
#             ans=mid
#             lo=mid+1
#         else:
#             hi=mid-1
#     temp=points[ans]
#
#     return temp
# def just_larger(points,val):
#     #print(val)
#     lo, hi = 0, len(points) - 1
#     ans = -1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if points[mid] >= val:
#             ans = mid
#             hi = mid - 1
#         else:
#             lo = mid + 1
#     temp=points[ans]
#     points.insert(ans,val)
#
#     return temp

x,n=[int(x) for x in input().split()]
p=[int(x) for x in input().split()]
points=[0,x]
pp=SortedList()
pp.add(0)
pp.add(x)
sl = SortedList()
sl.add(x-0)
for i in p:

    a=pp[pp.bisect_right(i)-1]
    b=pp[pp.bisect_left(i)]
    pp.add(i)
    #print(pp,i,a,b)
    gap=b-a
    sl.remove(gap)
    sl.add(b-i)
    sl.add(i-a)
    print(sl[-1],end=" ")




