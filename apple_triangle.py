word="APPLE"
count=len(word)
for i in range(count+1):
    for j in range(count-i):
        print(" ",end="")
    for k in range(i):
        print(word[k],end=" ")
    print()