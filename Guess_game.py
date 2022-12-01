while(True):
    while(True):
        i = 5
        n = 19
        print("\n You have altogether 5 guess \n")
        a = int(input("Guess one number and you will be guided thorougly: "))
        # i = i - 1
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
                print("Congratulations! You have guessed it in ", 6-i ,"chance ")
                break
        if i == 0:
            print("GAME OVER! You have lost all your chances")       
        Play_Again = input("\n Do you want to play again? (y/n) : ")
        if Play_Again == "y":   
            continue 
        else:
            print("\n Thank You! \n")
            break
        break
    break