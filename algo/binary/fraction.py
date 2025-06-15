import sys
import heapq
for _ in range(int(sys.stdin.readline())):
    def check(x):
        min_heap = []  # Min heap to store the top k elements

        # Push the first k elements onto the heap
        for i in range(k):
            num=arr1[i]-x*arr2[i]
            heapq.heappush(min_heap, num)

        # Iterate over the remaining elements

        for i in range(k,len(arr1)):
            num=arr1[i]-x*arr2[i]
            # If the current element is greater than the smallest element in the heap
            if num > min_heap[0]:
                # Pop the smallest element and push the current element onto the heap
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        # Sum up the elements in the heap
        result = sum(min_heap)
        return result>=0






    n, k = map(int, sys.stdin.readline().split())
    arr1 = list(map(int, sys.stdin.readline().split()))
    arr2 = list(map(int, sys.stdin.readline().split()))
    lo,hi=0,10**8
    ans=-1
    while hi-lo>=10**-7:
        mid=(lo+hi)/2
        #print(lo," ",mid," ",hi," ",check(mid))
        if check(mid):
            ans=mid
            lo=mid

        else:
            hi=mid

    print("{:.6f}".format(round(ans, 6)))