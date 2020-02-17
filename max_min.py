a=list(map(int,input("Enter:").split()))
maxi=a[0]
mini=a[0]
for i in range(len(a)):
    if(mini>a[i]):
        mini=a[i]
    if(maxi<a[i]):
        maxi=a[i]
print ("max=",end=" ")
print(maxi)
print ("min=",end=" ")
print(mini)


    
