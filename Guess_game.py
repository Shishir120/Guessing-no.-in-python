while(True):     #just to try the new thing specifically pull request

    i = 4
    while(True):
        i = 4
        n = 19
        print("\n You have altogether 5 guess \n")
        a = int(input("Guess one number and you will be guided thorougly: "))
        if a == n:
            print("\n WOW! You did it in your first guess \n")
            break
        while(i > 0):
            if a > 19:
                print("Oops! Your number is High")
                print("You have", i , "Chance left \n")
                a= int(input("Try Guessing Again: "))
                i = i - 1
            if a < 19:
                print("Oops! Your number is less")
                print("You have", i , "Chance left \n")
                a = int(input("Try Guessing Again: "))
                i = i - 1 
            if a == n:
                print("Congratulations! You have guessed it in", 5-i ,"chance ")
                break
        if i == 0 and a != n:
            print("GAME OVER! You have lost all your chances")       
        break
    Play_Again = input("\n Do you want to play again? (y/n) : ")
    if Play_Again == "y":   
        continue 
    else:
        print("\n Thank You! \n")     
        break
    break