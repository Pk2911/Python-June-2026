#turn a list into a string



user = input("enter the strings:").split() 
print(user)
sentence=""
for i in user:
    sentence = sentence + i + " "
print(sentence)