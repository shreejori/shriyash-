numbers=[0,1,0,3,12,0,5]
print(numbers)
zero=[]
a=0
for i in numbers:
    if i!=0:
        zero.append(i)
    else:
        a=a+1
for i in range(a):
    zero.append(0)

    print(zero)