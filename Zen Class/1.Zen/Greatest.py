a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=int(input("Enter number c:"))
if(a>b):
	if(a>c):
		greatest=a
	else:
		greatest=c
else:
	if(b>c):
		greatest=b
	else:
		greatest=c
print("The greatest number is =",greatest)
