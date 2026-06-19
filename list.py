#list 

#collection of data

# a=[2,3,4,5,6]

#properties
#1.list can have any element of any size
#data=[1,2.2,'mohan',True,[2,3,4]]

# #2.lists are ordered
# a=[1,2,3,4]
# b=[3,2,1,4]
# print(a==b)
# O/p=False

#3. lists,str,tuple are indexed
# a=[11,12,13,14,15,16,17,18]
# print(a[1:3])
# print(a[2:7:2])
# print(a[:7])
# print(a[3:])
# print(a[::-1])
# print(a[-1]==a[7])

# same w string,it includes spaces too

#4.lists are mutable
#str are immutable

# a=[1,2,3,4,5]
# a[0]='mohan'
# print(a)
# #works

# b='mohan'
# b[0]='h'
# print(b)
# #doenst work

#5.dynamic

#6. lists aare nested

# a=[1,2,[100,120],3,4]
# print(a[2])
# print(a[2][0])

#inbuilt methods

#to add elements 

# append() - adds an element to the end of the list
# a=[1,2,3,4]
# a.append(100)
# a.append(200)

# extend() - adds an iterable(anything which has a collection of elements to the list
# a=[1,2,3,4]
# a.extend([23,24,'mohan'])
# a.extend('hari')
# print(a)

# insert(index,value)
# a=[1,2,3,4]
# a.insert(0,'mohan')
# a.insert(2,[1,2,3,4])
# print(a)


#to remove elements

#remove() - remove element directly

#pop()

# a=[11,12,13,14,15,16,17]
# a.pop()
# a.pop(0)
# a.pop(0)
# a.pop(3)
# print(a)


#Tuple-also a collection of data

# a=(1,2,,'mohan',2.2)
#ordered
#indexed
#immutable

# a=(1,2,3,4)
# a[0]=10
# print(a)
# TypeError: 'tuple' object does not support item assignment

#iteration

# a=[11,22,33,44,55]
# b="mohandas"
c=(11,12,13,14,15)
for i in c:
    print(i,end=" ")
# print(len(b))

# for i in range(0,len(b)):
#     print(i,b[i])

fruits=['apple','mango','banana','melon']
for i in range(len(fruits)):
    print(i,fruits[i])


