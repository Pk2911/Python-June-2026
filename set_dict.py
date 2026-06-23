#set -collection of data

# a={3,4,5,6}

#unordered
#no index
#contains no duplicate values
# a={1,2,3,4,5,5,6,6}
# b={3,2,4,1,5,5,6,6}
# print(a==b)
# print(a)
# c=set(a)
# print(c)
# #True

# fruits={"mango","orange","apple","grapes","banana"}
# name={"sivdutt","ajel"}
# for i in fruits:
#     for j in name:
#         print(j+" "+i)
# # o/p- different order all the time

#sets are mutable - union , intersection, difference
# a={1,2,3,4,5,6}
# b={4,5,6,7,8,9}
# print(a.union(b))
# print(a|b)#same as above
# print(a.intersection(b))
# print(a&b)#same as above
# print(a-b)
# print(b-a)

#dict
#key value paired datatype
#key:"value"
# userdata={"name":"mohan","age":21,"location":"mvk"}
# print(type(userdata))

#index illa but mutable
# print(userdata["age"])
# print(userdata["location"])
#dict has more priority than set

# data={}
# data['name']='das'
# data["age"]=21
# data["place"]="mvk"
# data["phone"]="9778443548"
# data["name"]="pankaj"
# print(data)

#restrictions
#1.keys are unique
# 2.keys are ummutable type(cant use list set dict)

# inbuilt functions
# a={"name":"pk","age":21,"loc":"kochi"}
# print(a.get("name"))#OR
# print(a["loc"])
# print(a.keys())
# print(a.values())
# print(a.items())
# a.update({"loc":"mvk"})
# a.pop("name")
# a.popitem()
# # a.clear()
# print(a)

# data={"name":"pk","age":21,"loc":"kochi"}
# for i in data:
#     print(i,data[i])

# for i in data.keys():
#     print(i)

# for i in data.values():
#     print(i)

# for i in data.items():
#     print(i)

# for i,j in data.items():
#     print(f"{i}-{j}")

# a="my name is pk"
# b=a.split("a") #Or b=a.split()
# print(b)

#OR

# a="my name is pk"
# b=[]
# word=""
# for i in a:
#     if i !=" ":
#         word=word+i
#     else:
#         b.append(word)
#         word=""
# b.append(word)

# print(b)

