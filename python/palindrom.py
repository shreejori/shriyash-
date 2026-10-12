def palindrome(a,b,c):
    if b>=c:
      return True
    if a[b] != a[c]:
       return False
    return palindrome(a,b+1,c-1)
a="racecar"
print(palindrome(a,0,len(a)-1))