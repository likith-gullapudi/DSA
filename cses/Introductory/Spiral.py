for _ in range(int(input())):
    x,y=[int(x) for x in input().split()]
    completed = 0
    if x>=y:
        completed+=(x-1)**2
        #now we have to find y th column in xth row
        #have to check does it come under even or odd row
        if x&1==0:
            completed+=x
            completed+=(x-y)

        else:
            completed+=y

    else:
        completed+=(y-1)**2
        if y&1==0:
            completed+=x
        else:
            completed+=y
            completed+=(y-x)
    print(completed)




