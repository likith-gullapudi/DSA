n=int(input())
two_count=five_count=0
while n&1==0:
    n//=2
    two_count+=1
while n%5==0:
    n//=5
    five_count+=1
print(two_count,five_count)




