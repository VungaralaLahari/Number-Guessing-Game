import random 
n=random.randint(1,100)

while True:
    user=int(input("Enter your guess:"))
    
    if user==n:
        print("You guessed right!!!!!!")
        break
    
    elif user<n:
        print("You guessed a small number")
    
    elif user>n:
        print("You guessed a bigger number")

print("----------GAME OVER---------------")