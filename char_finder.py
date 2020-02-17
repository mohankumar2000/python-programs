str1="hi this is abc from chennai abc"
a=list(str1.split(" "))
print(a)
for i in range(len(a)):
    if(a[i]=="abc"):
        print("found",end=" ")
        print(a[i],end=" ")
        print("at index=",end=" ")
        print(i)
        
