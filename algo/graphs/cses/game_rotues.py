s='My name is lIKITH.My name is prasanth.'
temp=s.split('.')
temp2=[]
for i in temp[::-1]:
    temp2.append(i)
for sentence in temp2[1:]:
    s=sentence.split(' ')
    #print(s[::-1])
    print(' '.join(s[::-1]),end=".")
