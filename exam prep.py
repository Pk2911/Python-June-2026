# a=input("num:")
# count=len(a)
# digit=int(a)
# temp=digit
# sum=0
# while temp>0:
#     temp_n=temp%10
#     sum=sum+(temp_n**count)
#     temp=temp//10
# print(sum)

# triangle
# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#             print("*",end=" ")
#     print()



# user=[6,3,9,2,10]



# for i in range(len(user)):
#     if user[i]>largest:
#         largest=user[i]
#     if user[i]<smallest:
#         smallest=user[i]

# print(largest)
# print(smallest)

# for j in range(len(user)):
#     for k in range(len(user)-1):
#         if user[k] > user[k+1]:
#             user[k],user[k+1]=user[k+1],user[k]
# print(user)

# num=100
# a=str(num)
# rev=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
# print(rev)


# n=int(input("buebf:"))
# sum=0
# for i in range(n):
#     num=int(input("noum:"))
#     sum=sum+num
# print(sum)
# avg=sum/n
# print(avg)

# rows=10
# cols=7
# for i in range(rows):
#     for j in range(cols):
#         if i==0 or i==rows//2 or j==0 or (j == cols - 1 and i <= rows // 2):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# a={1,1,2,3,4,4}
# print(a)
# n=len(a)
# print(n)

#print a hollow square

# rows=8
# cols=8
# for i in range(rows):
#     for j in range(cols):
#         if (i==0 or i==rows-1 or j==0 or j==cols-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


for i in range(8):
    for j in range(8):
        if (i==0 or i==3 or i==7)or(i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#diagonqal S