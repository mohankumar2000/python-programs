print("****Welcome to ABC Bank****")
initial_amount=0.0
def home():
    n=1
    global initial_amount
    while(n==1):
        print("1.Deposit  2.Withdraw 3.Balance Enquiry  4.quit")
        a=int(input())
        if(a==1):
            dep()
            n=1
        elif(a==2):
            withdraw()
            n=1
        elif(a==3):
            print("Your account balance is:",end=" ")
            print(initial_amount)
            n=1
        elif(a==4):
            print("Thank you for using our bank")
            break
            n=0
        elif(a>=5 or a<1):
            print("choose valid choice:")
            n=1

def dep():
    print("Enter the amount to be add:")
    d=float(input())
    global initial_amount
    initial_amount=initial_amount+d
    print("Amount has been added successfully!!")
    print("Your account balance is: ",initial_amount)


def withdraw():
    print("Enter the amount to be withdraw:")
    w=float(input())
    global initial_amount
    if(w>initial_amount):
        print("OOPS!! your account does not have enough amount")
        home()
    else:
        initial_amount=initial_amount-w
        print("Amount has been withdraw successfully!!")
        print("Your account balance is: ",initial_amount)

home()
        
    
