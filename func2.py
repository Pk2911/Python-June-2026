#pep8-is a standard for pyhton


#lambda FUNCTION

#lambda arguements : expression
ans= lambda x,y:x+y
print(ans(2,3))

#product of 3 nos
ans=lambda x,y,z:x*y*z
print(ans(2,3,2))

#square of a num
ans=lambda x:x**2
print(ans(3))

#perimeter of a circle
ans=lambda r:2*3.14*r
print(ans(5))

#area of a triangle
ans=lambda b,h:(0.5*b*h)
print(ans(2,3))

#avg of 5 nos
ans=lambda x,y,z,a,b:(x+y+z+a+b)/5
print(ans(1,2,3,4,5))

#square root of a num
ans=lambda x:x**0.5
print(ans(25))
print(type(ans))

#full name of a person
ans=lambda fname,mname,lname:fname+" "+mname+" "+lname
print(ans("p","n","l"))

check=lambda age:"eligible" if age>=18 else "not eligible"
print(ans(21))