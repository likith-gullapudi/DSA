from sortedcontainers import SortedList
n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
class map:
    def __init__(self):
        self.a=SortedList()
        self.b=SortedList()
        self.a_sum=0
        self.b_sum=0
    def insert(self,val):
        if self.a and val>self.a[-1]:
            self.b.add(val)
            self.b_sum+=val
        else:
            self.a.add(val)
            self.a_sum+=val
        self.adjust()
    def remove(self,val):
        if val>self.a[-1]:
            self.b.remove(val)
            self.b_sum-=val
        else:
            self.a.remove(val)
            self.a_sum-=val
        self.adjust()

    def adjust(self):
        while len(self.b) > len(self.a):
            temp = self.b.pop(0)
            self.b_sum-=temp
            self.a.add(temp)
            self.a_sum+=temp
        while len(self.b) + 1 < len(self.a):
            temp = self.a.pop(-1)
            self.a_sum-=temp
            self.b.add(temp)
            self.b_sum+=temp

    def median(self):
        self.adjust()
        return self.a[-1]
    def cost(self):
        med=self.median()
        return (med*len(self.a)-self.a_sum)+(self.b_sum-med*len(self.b))


obj=map()
for i in range(k):
    obj.insert(arr[i])
# median=obj.median()
print(obj.cost(),end=" ")
for i in range(k,n):
    obj.remove(arr[i-k])
    obj.insert(arr[i])
    print(obj.cost(),end=" ")
