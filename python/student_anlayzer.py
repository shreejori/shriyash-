def analyze_marks(*args):
    if len(args)==0:
        print("no marks supplied")
        return

    total=0
    highest=args[0]
    passing=0
    for marks in args:
        total+=marks
        if marks>highest:
            highest=marks
        if marks >=40:
            passing+=1
    average=total/len(args)
    print("total",total)
    print("average",average)
    print("highest",highest)
    print(passing)
analyze_marks(70,85,35,90,45)