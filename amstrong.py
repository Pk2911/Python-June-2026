num=int(input("enter your number:"))
num_c=len(str(num))
am=0
temp=num
while temp>0:
    i=temp%10
    am=am+i**num_c
    temp=temp//10

if am==num:
    print('yay')
else:
    print("aww")