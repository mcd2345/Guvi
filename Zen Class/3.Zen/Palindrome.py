##Palindrome String

str=input()
j=len(str)-1
a=0
for i in range(0,len(str)):
    if(i<j):
        if(str[i]!=str[j]):
            a=1
        break
    j=j-1
if(a==1):
    print("Not Palindrome")
else:
    print("Palindrome String")