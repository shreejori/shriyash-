numbers=[1,1,2,2,2,3,3,1,1,1,1]
print(numbers)
count=1
max_count=1
for i in range(1,len(numbers)):
    if numbers[i] == numbers[i-1]:
        count+=1
    else:
        count=1
    if count > max_count:
        max_count=count
print(max_count)