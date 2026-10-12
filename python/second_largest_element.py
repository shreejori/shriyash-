numbers=[12,35,1,10,34,35]
print(numbers)
largest=numbers[0]
second_largest=-1
for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i
    elif i<largest:
        if i>second_largest and i!=largest:
            second_largest=i
            print(second_largest)