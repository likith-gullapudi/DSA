def fun(arr,k):
	n=len(arr)
	prefix_sum=[0 for i in range(n)]
	prefix_sum[0]=arr[0]%2
	for i in range(1,n):
		prefix_sum[i]+=prefix_sum[i-1]+arr[i]%2
	#print(prefix_sum)
	ans=0
	d={0:1}
	for i in prefix_sum:
		if i-k in d:
			ans+=d[i-k]

		d[i]=d.get(i,0)+1
		#print(d,ans)
	return ans

arr=[2,4,6]
k=1
print(fun(arr,k))