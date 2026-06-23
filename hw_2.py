#turn strings which are in a list into a complete string



user = input("enter the strings:").split() 
print(user)
sentence=""
for i in user:
    sentence = sentence + i + " "
print(sentence)