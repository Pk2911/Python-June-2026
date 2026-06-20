#string 

# #sequence of series
# ''
# ""
# ''''''
# name= "mohan"
# print(name)
# print(type(name))

# data= '''love is in the air so let's "rock and roll babyyy"'''
# print(data) 
# data= '''love is in the air so let's "rock and roll babyyy"'''
# print(data) 

#escape sequence

# \' - - '
# \" - - "
#\n - new line
#\t - tab space
#\b - backspace

# data=  'love is in the air\nso let\'s "rock \'n\' roll baby"'
# print(data)

# data = " googoo\\n \n gaagaa\\b "
# print(data)
# #raw string 
# data1 = r"love is in the air\n \n \t \b."
# print(data1)

#input function
# input() - returns string
#string concantention
# a=input("enter smtg")
# b=input("enter smtg")
# print(a+b)
# print(a+" " +b)

#type conversion/casting

#implicit
#explicit

# a= float(input("enter a no"))
# b = int(input("enter another"))
# print(a+b)

#string format

# name=input("enter name:")
# age= int(input("enter age:"))
# married_status = (input("enter status:"))
# rating = float(input("enter rating:"))

# bio = f"my name is {name}\nmy age is {21}\nand i m eligible for marraige but my current status is {married_status},\nand my rating is {rating}"
# print(bio)

#control statement

#loops

#while

#comdition based loop
#infinite loop

# while True:
#     print("pk")

# i=1
# print("sivdutt & ajel")
# while i < 6:
#     print(i)
#     i = i + 1
# print("mohan")
# print("pk")    

# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     #print(sum)
#     i=i+1
# print(sum)

# i=0
# sum_even=0
# sum_odd=0
# while i<=100:
#     if i%2==0:
#         sum_even=sum_even + i
#     else:
#         sum_odd=sum_odd + i
#     i=i+1

# print(sum_even,sum_odd)


#sum of digits in a number

#input - 343
#o/p - 10

# num=int(input("enter your number:"))
# sum=0
# while num>0:
#     sum=sum+num%10
#     num=num//10
# print(sum)

#reverse of a number

# num=int(input("enter your number:"))
# reversed=0
# while num>=0:
#     reversed=reversed*10+num%10
#     num=num//10
# print(reversed)


#factorial of a num

# num=int(input("enter your number:"))
# fac=1
# while num>0:
#     fac*=num
#     num-=1
# print(fac)

