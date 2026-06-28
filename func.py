# a=[1,2,3,4,55,66,77]
# b=[]
# c=[]
# mid=(len(a)+1)//2

# for i in a:
#     if i>mid:
#         c.append(i)
#     else:
#         b.append(i)

# print(b)
# print(c)


# a=[11,1,100,-900,10,15,16]
# largest=0
# smallest=0

# for i in a:
#     if i>largest:
#         largest=i
#     if i<smallest:
#         smallest=i

# print(largest,smallest)


#functions
#block of code which is executed when its called.

# def functioname(<arguements>):
#     #then code to be executed

def hello():
    print("hello good morro!!")
hello()
#DRY - dont repeat yourself

#structural programming
#functional programming - imp for interview
#procedural programming

# arguements - values to be passed to a function

# def add(a,b):
#     print(a+b)

# add(2,3)
# add("c","d")

# 1.positional arguements


# def add(a,b):
#     print(a+b)

# add(2,3)

# 2.keyword arguements

def fullname(fname,mname,lname):
    print(fname+' '+mname+' '+lname)
fullname(lname='jr',fname='robert',mname='downey')

#default arguement
# def add(a=0,b):
# SyntaxError: parameter without a default follows parameter with a default

# def add(a=0,b):
# SyntaxError: parameter without a default follows parameter with a default

def add(a=0,b=0):
    print(a+b)

add(6,6)
