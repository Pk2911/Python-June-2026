#nested loops

# for i in range(1,6):
#     for j in range(1,6):
#         for k in range(1,6):
#             print(i,j,k)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(6,0,-1):
#     for j in range(i+1,1,-1): #or (i)
#         print("*",end="")
#     print()

# upside down triangle
# for i in range(5,0,-1):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#             print("*",end=" ")
#     print()

# # triangle
# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#             print("*",end=" ")
#     print()

# print chessboard pattern

# for i in range(1,9):
#     for j in range(1,9):
#         if (i+j)%2==0: #or if (i%2==0)==(j%2==0)
#             print("W",end=" ")
#         else:
#             print("B",end=" ")
#     print()

# rows=7
# col=5
# for i in range(rows):
#     for j in range(col):
#         if i==0 or i==rows-1 or j==col//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

rows=7
col=7
for i in range(rows):
    for j in range(col):
        if j==0 or j==col-1 or i==rows//2:
                print("*",end=" ")
        else:
                print(" ",end=" ")
    print()
