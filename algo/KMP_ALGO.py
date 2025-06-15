def kmp_algo(s,n):
    pi=[-1 for i in range(n+1)]
    i,j=0,-1
    while i<n:
        while j!=-1 and s[i]!=s[j]:
            j=pi[j]
        i+=1
        j+=1
        pi[i]=j
    return pi[1:]