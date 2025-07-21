n,w,h=[int(x) for x in input().split()]
cards=[(w,h,0)]
d={}
for _ in range(n):
    ww,hh=[int(x) for x in input().split()]
    if ww<=w or hh<=h:
        continue
    cards.append([ww,hh,_+1])

cards.sort(key=lambda x:x[0])
n=len(cards)
#dp[i] number of envelopes from range 0 to i
#base case dp[i]=1
#

dp=[0 for i in range(n)]
path=[-1 for i in range(n)]
dp[0]=1
for i in range(1,n):
    for j in range(i):

        if cards[i][1]>cards[j][1] and cards[i][0]>cards[j][0]:
            if dp[i]<1+dp[j]:
                dp[i]=1+dp[j]
                path[i]=j

ans=-1
index=-1
for i,val in enumerate(dp):
    if val>ans:
        ans=val
        index=i
print(ans-1)
res = []
while index != -1 and index != 0:
    res.append(cards[index][2])
    index = path[index]

print(' '.join(map(str, reversed(res))))


