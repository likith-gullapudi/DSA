#find prime numbers from 1 to 2n  using
def prime_numbers(n):
    check=[True for i in range(n+1)]
    i=2
    while i<n:
        if check[i]:
            for imultiple in range(i+i,n+1,i):
                check[imultiple]=False
        i+=1
    primes=set()
    for i in range(2,n+1):
        if check[i]:
            primes.add(i)
    return primes
n=int(input())
d={i:1 for i in range(1,n+1)}
primes=prime_numbers(2*n)
ans=[]
a={}
for i in range(1,n+1):
    for j in range(i+1,n+1):
        s=i+j
        if i+j in primes:
            if i+j in a:
                a[i+j].append([i,j])
            else:
                a[(i+j)]=[[i,j]]








s=set()
def rec(index):
    print(index,ans)
    global count
    #base_case
    if index==n-1:
        count+=1



        return
    #choices
    for ch,x in a.items():
        for li in x:
            if d[li[0]]>0 and d[li[1]]>0:
                ans.append(ch)
                d[li[0]]-=1
                d[li[1]]-=1
                rec(index+1)
                ans.pop()
                d[li[0]] += 1
                d[li[1]] += 1

rec(0)
print(len(ans))





