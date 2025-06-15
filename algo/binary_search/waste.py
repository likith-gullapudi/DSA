ans=2
def fun(i):
    global ans
    if i==0:
        ans=3
        return
    fun(i-1)
fun(3)
print(ans)