def rec(index):

    if index==len(word):
        return True
    s=""
    for z in range(index,len(word)):
        s+=word[z]
        if s in d:
            if rec(z+1):
                return True

    return False



for _ in range(int(input())):
    n=int(input())
    word=input()
    d=set()
    for _ in range(n):
        d.add(input())
    print("YES" if rec(0) else "NO")