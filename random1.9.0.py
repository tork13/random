import random
import math
gamemode = "nothing"
chooseGame = 'nothing'
play = "yes"
while (play=="yes"):
    count = 0
    count2 = 0
    count3 = 1
    while (chooseGame == "nothing"):
        play = input("Do you want to play (yes/no)?")
        if(play == "no"):
            break
        chooseGame = input("What game do you want to play.\nMastermind(MA)\nRandom Number Generator(R)\nDeal or no Deal (D)\nHigher/Lower(N)?\n")
        chooseGame = chooseGame.upper()
        while(chooseGame != "MA" and chooseGame != "D" and chooseGame != "N" and chooseGame != "R"):
            chooseGame = input("That's not a choice pick again.\nMastermind(MA)\nRandom Number Generator(R)\nDeal or no deal (D)\nHigher/Lower(N)\n")
            chooseGame = chooseGame.upper()
#random number 
        if(chooseGame == "R"):
        	sim = input("Flip a coin(F)\nRandom number(R)\nDice(D)\n")
        	sim = sim.upper()
        	while(sim != "F" and sim != "R" and sim != "D"):
        		sim = input("Sorry that is not a choice. Pick again.\nFlip a coin(F)\n Random number(R)\n Dice(D)\n")
        		sim = sim.upper()
        	if(sim == "F"):
        		agian = "Y"
        		while(agian == "Y"):
        			coin = random.randrange(0,2)
        			if(coin == 1):
        				print("heads")
        				agian = input("agian (y/n)")
        				agian = agian.upper()
        			elif(coin == 0):
	        			print("tails")
        				agian = input("agian (y/n)")
        				agian = agian.upper()
        			if(agian == "N"):
        				chooseGame = "nothing"
        				sim = "nothing"
        	while(sim == "R"):
        		first = int(input("Pick your start number"))
        		second = int(input("pick your end number"))
        		while(first >= second):
        			second = int(input("error: second number must be bigger\n re-enter please"))
        		randnumber = random.randrange(first,second)
        		print("your random number is", randnumber)
        		repeat = input("again?(y/n)")
        		repeat = repeat.upper()
        		if(repeat == "N"):
        			sim = "nothing"
        			chooseGame = "nothing"
        	while(sim == "D"):
        		amount = int(input("how many dice"))
        		sides = int(input("how many sides on each die"))
        		for i in range (amount):
        			print("dice",i + 1,"is",random.randrange(1,sides+1))
        		repeat2 = input("again? (y/n)")
        		repeat2 = repeat2.upper()
        		if(repeat2 == "N"):
        			sim = "nothing"
        			chooseGame = "nothing"
        
#Mastermind
        if (chooseGame == "MA"):
            game = True
            print (" --- MASTERMIND --- \n")
            print ("Guess the secret color code in as few tries as possible.\n It is four colors long.")
            colornum = int(input("How many colors do you want to play with?\n The more colors the harder it is\n(6/7/8/9/10)"))
            if (colornum == 6):
                    print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W) and pink(P)")
                    colors = ["R", "G", "B", "Y", "W", "P"]
            elif(colornum == 7):
                    print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W), pink(P) and orange(O)")
                    colors = ["R", "G", "B", "Y", "W", "P","O"]
            elif(colornum == 8):
                    print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W), pink(P),orange(O),Black(K),")
                    colors = ["R", "G", "B", "Y", "W", "P","O","K"]
            elif(colornum == 9):
                    print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W), pink(P),orange(O),Black(K),brown(R)")
                    colors = ["R", "G", "B", "Y", "W", "P","O","K","R"]
            elif(colornum == 10):
                    print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W), pink(P),orange(O),Black(K),brown(R), and purple(U)")
                    colors = ["R", "G", "B", "Y", "W", "P","O","K","R","U"]
            print("'X' means a color is in the correct spot\n an 'O' means a color is in an incorrect spot.\n You have 6 tries good luck!")
            attempts = 0
            color_code = random.sample(colors,4)		
            game2 = True
            while (game2):
                    correct_color = ""
                    guessed_color = ""
                    player_guess = input().upper()
                    attempts += 1
                    if len(player_guess) != len(color_code):
                            print ("\nThe secret code has exactly four colors. I know, you can count to four. Try again!")
                            continue
                    for i in range(4):
                            if player_guess[i] not in colors:
                                    print ("\nLook up what colors you can use in this game. You are not a daltonist, are you?")
                                    continue
                    if correct_color != "XXXX":
                            for i in range(4):
                                    if player_guess[i] == color_code[i]:
                                            correct_color += "X"
                                    elif  player_guess[i] != color_code[i] and player_guess[i] in color_code:
                                            guessed_color += "O"
                            print (correct_color +  guessed_color + "\n")		
                            
                    if correct_color == "XXXX":
                            if attempts == 1:
                                    print ("Wow! You guessed at the first attempt!")
                            else:
                                    print ("Well done... You needed " + str(attempts) + " attempts to guess.")
                            game = False
                            game2 = False
                            
                    if attempts >= 1 and attempts <6 and correct_color != "XXXX":
                            print ("Next attempt: ")
                    elif attempts >= 6:
                            print ("You didn't guess it! The secret color code was: " + str(color_code))
                            game = False

                    while game == False:
                            finish_game = input("\nDo you want to play again (Y/N)?").upper()	
                            attempts = 0
                            if finish_game =="N":
                                    print ("Thanks for playing!")
                                    chooseGame = "nothing"
                                    game = True
                            elif finish_game == "Y":
                                    game = True
                                    print ("So, let's play again... Guess the secret code: ")
                                    
                
#Deal or no deal
        if(chooseGame == "D"):
            amounts = [1, 5, 10, 25, 50, 100, 250, 500, 1000]
            shuffledamounts = random.shuffle(amounts)
            start = 1
            while (start == 1):
                print("Welcome to Deal or No Deal. You can win $1, $5, $10, $25, $50, $100, $250, $500, $1000. Good luck!")
                yourCase= int(input("Pick a case 1-9. This will be your case. "))
                while(yourCase<1 or yourCase>9):
                    yourCase= int(input("USER ERROR: Pick a case 1-9. This will be your case. "))


                if(amounts[yourCase -1] == 1000):
                    choice1 = int(input("Pick a case between 1 and 9 that you have not chosen already:"))
                else:
                    choice1 = int(input("Pick a case between 1 and 9 that you have not chosen already: "))
                while(yourCase == choice1 or choice1<1 or choice1>9):
                    choice1 = int(input("USER ERROR: Pick a case between 1 and 9 that you have not chosen already: "))
                print("$",amounts[(choice1-1)], "is off the board")
                choice2 = int(input("Pick a case between 1 and 9 that you have not chosen already: "))
                while(yourCase == choice2 or choice1 == choice2 or choice2<1 or choice2>9):
                    choice2 = int(input("USER ERROR: Pick a case between 1 and 9 that you have not chosen already: "))
                print("$",amounts[(choice2-1)], "is off the board")
                choice3 = int(input("Pick a case between 1 and 9 that you have not chosen already: "))
                while(yourCase == choice3 or choice1 == choice3 or choice2 == choice3 or choice3<1 or choice3>9):
                    choice3 = int(input("USER ERROR: Pick a case between 1 and 9 that you have not chosen already: "))
                print("$",amounts[choice3-1], "is off the board")
                choice4 = int(input("Pick a case between 1 and 9 that you have not chosen already: "))
                while(yourCase == choice4 or choice1==choice4 or choice2==choice4 or choice3==choice4 or choice4<1 or choice4>9):
                    choice4 = int(input("USER ERROR: Pick a case between 1 and 9 that you have not chosen already: "))
                print("$",amounts[choice4-1], "is off the board")
                offer1= (1941- amounts[choice1-1] - amounts[choice2-1] - amounts[choice3-1] - amounts[choice4-1])/5
                print("Your offer is $",offer1,".")
                question1= input("Do you accept or decline the offer from the bank? (a/d) ")
                while(question1 != "a" and question1 != "d"):
                    question1= input("USER ERROR: Do you accept or decline the offer from the bank? (a/d) ")
                if(question1 == "a"):
                    print("Congratulations, you won $",offer1,"!")
                    start = "nothing"
                    chooseGame = "nothing"
                else:
                    choice5 = int(input("Pick a case between 1 and 9 that you have not chosen already: "))
                    while(yourCase == choice5 or choice1==choice5 or choice2==choice5 or choice3==choice5 or choice4==choice5 or choice5<1 or choice5>9):
                        choice5 = int(input("USER ERROR: Pick a case between 1 and 9 that you have not chosen already: "))
                    print("$",amounts[choice5-1], "is off the board")
                    choice6 = int(input("Pick a case between 1 and 9 that you have not chosen already: "))
                    while(yourCase == choice6 or choice1==choice6 or choice2==choice6 or choice3==choice6 or choice4==choice6 or choice5==choice6 or choice6<1 or choice6>9):
                        choice6 = int(input("USER ERROR: Pick a case between 1 and 9 that you have not chosen already: "))
                    print("$",amounts[choice6-1], "is off the board")
                    offer2= (1941- amounts[choice1-1] - amounts[choice2-1] - amounts[choice3-1] - amounts[choice4-1]-amounts[choice5-1]-amounts[choice6-1])/5
                    print("Your offer is $",offer2,".")
                    question2= input("Do you accept or decline the offer from the bank? (a/d) ")
                    while(question2 != "a" and question2 != "d"):
                        question1= input("USER ERROR: Do you accept or decline the offer from the bank? (a/d) ")
                    if(question2 == "a"):
                        print("Congratulations, you won $",offer1,"!")
                        start = "nothing"
                        chooseGame="nothing"
                    else:
                        choice7 = int(input("Pick a case between 1 and 9 that you have not chosen already: "))
                        while(yourCase == choice7 or choice1==choice7 or choice2==choice7 or choice3==choice7 or choice4==choice7 or choice5==choice7 or choice6==choice7 or choice7<1 or choice7>10):
                            choice7 = int(input("USER ERROR: Pick a case between 1 and 9 that you have not chosen already: "))
                        print("$",amounts[choice7-1], "is off the board")
                        print("There are two values left. The value you chose at the beginning in case #",yourCase,"and the value of the case you haven't chosen")
                        print("Would you like to take the value in your original case (o), or the value in the case you have not chosen to open yet(r)?")
                        finalChoice=(input(""))
                        while (finalChoice !="o" and finalChoice !="r"):
                            finalChoice = (input("Try again:"))
                        if (finalChoice =="r"):
                            remcase = (45-(choice1+choice2+choice3+choice4+choice5+choice6+choice7+yourCase))
                            print("Congratulations! You won ${}!".format(amounts[remcase-1]))
                            chooseGame= "nothing"
                            start = "nothing"
                        else:
                            print("Congratulations! You won ${}!".format(amounts[yourCase-1]))
                            chooseGame= "nothing"
                            start = "nothing"

#Higher or lower
        if(chooseGame == "N"):
            gamemode = input ("Choose a gamemode: Infinite(I) or Challenge (C) or Multiplayer (M).")
            gamemode = gamemode.upper()
        while (gamemode =="I"):
            dif = int(input("What difficuly would you like to play on (1-10)?"))
            maximum= pow(10,dif)
            a = random.randrange(1,maximum)
            b = 0
            while (a != b):
                print("Guess number between 1 and", maximum,".")
                b = int(input(" "))
                if(b>a):
                    print("The number is lower")
                    count = count + 1
                elif(b<a):
                    print("The number is higher")
                    count = count + 1
            print("You won in", count, "tries.Score and leaderboards under construction")
            gamemode = "nothing"
            chooseGame = "nothing"
        while (gamemode == "C"):
            dif = int(input("What difficuly would you like to play on (1-6)?"))
            dif2 = int(input("How challenging should it be (1-10)?"))
            maximum= pow(10,(dif+4))
            a = random.randrange(1,pow(10,(dif+4)))
            b = 0
            count2=int(math.log2(maximum)-dif2)
            while (a > 0):
                print("Guess number between 1 and", maximum,". You have", count2 ,"guesses.")
                b = int(input(" "))
                if(a == b):
                    print("You won with", count2, "tries remaining. Score and leaderboards under construction.")
                    a = -1
                    gamemode = "nothing"
                    chooseGame = "nothing"
                else:
                    if (count2 == 1):
                        print('you lost. the number was',a,". Score and leaderboards under construction")
                        a = -1
                        gamemode = "nothing"
                        chooseGame = "nothing"
                    elif(b>a):
                        print("The number is lower")
                        count2 = count2 - 1
                        print("You have", count2, "guesses remaining.")
                    elif(b<a):
                        print("The number is higher")
                        count2 = count2 - 1
                        print("You have", count2, "guesses remaining.")
        while (gamemode == "M"):
            dif = int(input("What difficuly would you like to play on (1-10)?"))
            maximum= pow(10,dif)
            name1=input("Player 1, what is your name?")
            name2=input("Player 2, what is your name?")
            print(name1,", please pick a number between 1 and", maximum," that you know", name2,"will not guess. Make sure", name2, "is not looking.")
            c = int(input("What is the number?"))
            while((c > maximum) or ( c < 1)):
                print(" you're as stupid as jeremy put in another number")
                c = int(input("What is the number?"))
            d = 0
            counttt = 0
            while(counttt<40):
                counttt = counttt + 1
                print(" ")
            while (c != d):
                print("Guess number between 1 and", maximum,".")
                d = int(input(" "))
                if(d>c):
                    print("The number is lower")
                    count3 = count3 + 1
                elif(d<c):
                    print("The number is higher")
                    count3 = count3 + 1
            print("You won in", count3, "tries.Score and leaderboards under construction")
            gamemode = "nothing"
            chooseGame = "nothing"
