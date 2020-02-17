a=input()
for i in range(len(a)):
    if(a[i]=="@"):
        b=i
    if(a[i]=="."):
        c=i
    if(b<c):
        print("valid")
    else:
        print("not valid")
        
