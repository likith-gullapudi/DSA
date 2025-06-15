from sortedcontainers import SortedList
n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
class map:
    def __init__(self):
        self.a=SortedList()
        self.b=SortedList()
    def insert(self,val):
        if self.a and val>self.a[-1]:
            self.b.add(val)
        else:
            self.a.add(val)
        self.adjust()
    def remove(self,val):
        if val>self.a[-1]:
            self.b.remove(val)
        else:
            self.a.remove(val)
        self.adjust()

    def adjust(self):
        while len(self.b) > len(self.a):
            temp = self.b.pop(0)
            self.a.add(temp)
        while len(self.b) + 1 < len(self.a):
            temp = self.a.pop(-1)
            self.b.add(temp)

    def median(self):
        self.adjust()
        return self.a[-1]
obj=map()
for i in range(k):
    obj.insert(arr[i])
print(obj.median(),end=" ")
for i in range(k,n):
    obj.remove(arr[i-k])
    obj.insert(arr[i])
    print(obj.median(),end=" ")




