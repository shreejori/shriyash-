def analyze(numbers):
    total=0
    count=0
    largest=0
    for i in numbers:
        if i>=0 and i%2==0:
            square= i*i
            total+=square
            count+=1

            if square >largest:
                largest=square

    print("total",total)
    print("count",count)
    print("largest",largest)
numbers=[-2,1,2,3,4,6,-8]
analyze(numbers)