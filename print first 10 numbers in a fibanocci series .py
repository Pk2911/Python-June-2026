num=int(input("Enter your number:"))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    temp=a+b
    a=b
    b=temp

#  Output:   
# Enter your number:10
# 0 1 1 2 3 5 8 13 21 34 
