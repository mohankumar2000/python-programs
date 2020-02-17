print("welcome ")
a=1
while(a!=0):
    print("1=>college  2=>movie  3=>take test  4=>play games  q=>quit")
    print("Enter your choices:")
    b=(input())
    if(b=='q'):
        a=0
        print("Thank You")
    elif(int(b)>=5):
        print("Enter the correct value")
