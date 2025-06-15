import re
s='101001'
pattern=r'10*1'
results=re.finditer(pattern,s)
for ans in results:
    print(ans)
