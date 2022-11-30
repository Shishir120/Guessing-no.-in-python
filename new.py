n = 19
i = 5
print("You have altogether 5 guess")
a = int(input("Guess one number and you will be guided thorougly: "))
while(True):
    if a == n:
        print("WOW! You did it in your first guess")
        break
    while(i > 0):
        if a > 19 and a < 30:
            i= i - 1
            print("Oops! Your number is slightly more...")
            print("You have", i , "Guess left")
            a= int(input("Try Guessing Again: "))
        if a < 19 and  a > 10:
            i = i - 1 
            print("Oops! Your number is slightly less...")
            print("You have", i , "Guess left")
            a = int(input("Try Guessing Again: "))
        if a >= 30:
            i = i - 1
            print("Your number is very large")
            print("You have", i , "Guess left")
            a = int(input("Try Guessing Again: "))
        if a <= 10:
            i = i - 1
            print("Your number is very Small")
            print("You have", i , "Guess left")
            a = int(input("Try Guessing Again: "))
        if a == n:
            print("Congratulations! You have guessed it in ", 6-i ,"guess")
            break
    break    
if i == 0:
    print("Oops You have lost all your chances")            

