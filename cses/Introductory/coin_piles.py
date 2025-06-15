'''
a-2x-y=0=> 2x+y=a=>2x+y=a
b-x-2y=0=> x+2y=b=>2x+4y=2*b
3y=2*b-a=>(2*b-a)%3==0
'''

for _ in range(int(input())):
    a,b=[int(x) for x in input().split()]
    y = (2 * b - a) / 3
    x = (a - y) / 2
    if (2*b-a)%3==0 and x>=0 and y>=0:
        print("YES")
    else:
        print('NO')
    