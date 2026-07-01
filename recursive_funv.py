#higher order function
#when a function gets a function as its arguement
#or whenn a function returns a fucntion

#Recursion

#10 numbers
# def counttozero(n): #stub
#     print(n)
#     if n==0:
#         return
#     return counttozero(n-1)

# counttozero(10)


# def sum(n):
#     if n ==0:
#         return 0
#     return n * sum(n-1)
# print(sum(10))

#factorial
# def sum(n):
#     if n ==0:
#         return True
#     return n * sum(n-1)
# print(sum(10))



#Scope of a variable
# # scope - area in which it is recognized

name="pk" #global scope
def myname():
    #name="ajel" #local scope
    print(name)
    def nickname():
        name="kich" #enclosed scope
        print(name)
    nickname()

myname()

#L E G B -Local Enclosing Global Built-in function
