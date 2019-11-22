num=input()
num=int(num)
digit=0
while(num>0):
    a=temp%10
    digit+=a**len
    temp//=10
if(num==digit):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
    
