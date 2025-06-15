n,r=[int(x) for x in input().split()]
#ncr=(n!)/(r!)*(n-r)!=(n*(n-1)*(n-(r-1)))/(r*(r-1)*(r-(r-1))
num=den=1
for i in range(r):
    num*=(n-i)
    den*=(i+1)
print(num/den)
