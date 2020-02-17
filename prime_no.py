n=int(input())
for i in range(n):
    l=0
    if n>1:
        for j in range(2,i+1):
            if i%j==0:
               l=l+1
            else:
               pass
    if l==1:
       print(i)
