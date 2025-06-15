arr=[1,2,3]
for index,val in enumerate(arr[::-1]):
    print(len(arr)-index-1,val)