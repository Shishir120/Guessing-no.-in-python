n = 19
i = 5
print("\n You have altogether 5 guess \n")
a = int(input("Guess one number and you will be guided thorougly: "))
while(True):
    if a == n:
        print("\n WOW! You did it in your first guess \n")
        break
    while(i > 0):
        if a > 19:
            i= i - 1
            print("Oops! Your number is Greater")
            print("You have", i , "Chance left \n")
            a= int(input("Try Guessing Again: "))
        if a < 19:
            i = i - 1 
            print("Oops! Your number is less")
            print("You have", i , "Chance left \n")
            a = int(input("Try Guessing Again: "))
        if a == n:
            print("Congratulations! You have guessed it in ", 6-i ,"chance \n")
            break
    break    
if i == 0:
    print("GAME OVER! You have lost all your chances")            


