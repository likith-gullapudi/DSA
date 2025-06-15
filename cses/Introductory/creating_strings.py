s=input()
n=len(s)
fans=[set()]
def fun(s,ans):
    if s=='':
        fans[0].add(ans)
        return
    for i in range(len(s)):
        fun(s[:i]+s[i+1:],ans+s[i])
fun(s,'')
print(len(fans[0]))
temp=list(fans[0])
fans[0]=sorted(temp)
for i in fans[0]:
    print(i)


