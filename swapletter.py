n=input()
for i in range(0,len(n)):
    if ord(n[i])>=97 and ord(n[i])<=122:
        print(n[i].upper(),end="")
    else:
        print(n[i].lower(),end="")
