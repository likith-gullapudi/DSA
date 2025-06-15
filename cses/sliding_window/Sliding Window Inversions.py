from sortedcontainers import SortedList
n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
class Map:
    def __init__(self):
        self.l = SortedList()

    def insert(self, val):
        lesser = self.l.bisect_left(val)  # Elements strictly less than val
        greater = len(self.l) - self.l.bisect_right(val)  # Elements strictly greater than val
        self.l.add(val)
        return [lesser, greater]

    def remove(self, val):
        if val not in self.l:
            return [-1, -1]  # Or raise an error if desired
        lesser = self.l.bisect_left(val)
        greater = len(self.l) - self.l.bisect_right(val)
        self.l.remove(val)
        return [lesser, greater]
obj=Map()
count=0
for i in range(k):
    count+=obj.insert(arr[i])[1]
print(count,end=" ")
for i in range(k,n):
    count-=obj.remove(arr[i-k])[0]
    count+=obj.insert(arr[i])[1]
    print(count,end=" ")


