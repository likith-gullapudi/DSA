n=int(input())
time=[]
d=0
for _ in range(n):
    t,de=[int(x) for x in input().split()]
    d+=de
    time.append(t)
time.sort()
temp=0
prefix=0
for i in time:
    prefix+=i
    temp+=prefix
print(d-temp)


