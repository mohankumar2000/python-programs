print("****Welcome to ABC Bank****")
initial_amount=0.0
def home():
    n=1
    global initial_amount
    while(n==1):
        print("1.Deposit  2.Withdrawal  3.Balance Enquiry  4.Quit")
        a=int(input())
        if(a==1):
            deposit()
            n=1
        elif(a==2):
            withdrawal()
            n=1
        elif(a==3):
            print("Your account balance is:",end=" ")
            print(initial_amount)
            n=1
        elif(a==4):
            print("Thank you for using our bank")
            n=0
        elif(a>=5 or a<1):
            print("choose valid choice:")
            n=1

def deposit():
    global initial_amount
    print("Enter the amount to be add:")
    d=float(input())
    initial_amount=initial_amount+d
    print("Amount has been added successfully!!")
    print("Your account balance is: ",initial_amount)


def withdrawal():
    global initial_amount
    print("Enter the amount to be withdrawal:")
    w=float(input())
    if(w>initial_amount):
        print("OOPS!! Your account does not have enough amount")
        home()
    else:
        initial_amount=initial_amount-w
        print("Amount has been withdrawal successfully!!")
        print("Your account balance is: ",initial_amount)

home()
        
    
