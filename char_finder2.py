a=(input("Enter the string:").split())
b=input("Enter the word to be searched:")
for i in range(len(a)):
    if(a[i]==b):
        print("found",end=" ")
        print(a[i],end=" ")
        print("at index=",end=" ")
        print(i)
