a="listen"
b="silent"
if len(a) == len(b):
    for i in a:
        if a.count(i) != b.count(i):
            print("not anagram")
            break
    else:
            print("anagram")
else:
    print("not anagram")