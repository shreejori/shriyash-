a=[1,3,5]
b=[2,4,6]
c=[]
i=0
j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
print(c+a[i:]+b[j:])