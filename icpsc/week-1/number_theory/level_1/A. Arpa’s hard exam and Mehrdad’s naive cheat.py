n=int(input())
# for i in range(10):
#     print(i,8**i)
d=[6,8,4,2]
if n==0:
    print(1)
else:
    n%=4
    print(d[n])