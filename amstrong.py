# num=int(input("enter your number:"))
# num_c=len(str(num))
# am=0
# temp=num
# while temp>0:
#     i=temp%10
#     am=am+i**num_c
#     temp=temp//10

# if am==num:
#     print('yay')
# else:
#     print("aww")

# n=int(input("enter your number:"))
# prime=True
# if n<=1:
#     prime=False
# else:
#     for i in range(2,n):
#         if n%i==0:
#            prime = False
#         break

# if prime==True:
#     print("prime num")
# else:
#     print("not prime")

n=int(input("enter your number:"))
if n<=1:
    print("not prime or composite")
else:
    for i in range(2,n):
        if n%i==0:
           print("composite number")
        break
    else:
        print("prime number")