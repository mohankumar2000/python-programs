import random
print("welcome to number guessing game")
for i in range(5):
    print("Guess the number from 1 to10")
    print(i+1,end=" ")
    print("chance")
    a=int(input())
    b=random.randint(1,10)
    if(a==b):
        print("Congrats! You won")
        break
    else:
        print("oh no! You Lose")
    
